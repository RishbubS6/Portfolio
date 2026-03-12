import os
import json
import requests
from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

GOOGLE_API_KEYS = [v for k, v in sorted(os.environ.items()) if k.startswith('GOOGLE_API_KEY') and v]

def _safe_err(e):
    """Strip API keys from error messages before sending to client."""
    msg = str(e)
    for key in GOOGLE_API_KEYS:
        msg = msg.replace(key, '***')
    return msg


@app.route('/api/providers')
def get_providers():
    return jsonify({'google': bool(GOOGLE_API_KEYS)})


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    system = data.get('system', '')
    try:
        return jsonify({'content': _call_google(messages, system)})
    except Exception as e:
        return jsonify({'error': _safe_err(e)}), 500


@app.route('/api/stream', methods=['POST'])
def stream():
    data = request.json
    messages = data.get('messages', [])
    system = data.get('system', '')

    def generate():
        try:
            yield from _stream_google(messages, system)
        except Exception as e:
            yield f"data: {json.dumps({'error': _safe_err(e)})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'}
    )


@app.route('/api/image', methods=['POST'])
def image():
    import re
    prompt = request.json.get('prompt', '')
    prompt = re.sub(r'^(generate|create|draw|make|design|paint|render|imagine|show\s+me)\s+(an?\s+)?((image|picture|photo|illustration|art|painting|drawing|portrait|landscape)\s+(of\s+)?)?', '', prompt, flags=re.IGNORECASE).strip() or prompt
    size = request.json.get('size', '1024x1024')
    try:
        w, h = size.split('x') if 'x' in size else ('1024', '1024')
        encoded = requests.utils.quote(prompt)
        import base64, time
        # Try Gemini image models first
        img_models = ['gemini-2.5-flash-image', 'gemini-3.1-flash-image-preview', 'gemini-3-pro-image-preview']
        for model in img_models:
            for key in GOOGLE_API_KEYS:
                try:
                    r = requests.post(
                        f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}',
                        json={'contents': [{'parts': [{'text': prompt}]}],
                              'generationConfig': {'responseModalities': ['IMAGE', 'TEXT']}},
                        timeout=60
                    )
                    r.raise_for_status()
                    for part in r.json()['candidates'][0]['content']['parts']:
                        if 'inlineData' in part:
                            mime = part['inlineData']['mimeType']
                            b64 = part['inlineData']['data']
                            return jsonify({'url': f'data:{mime};base64,{b64}', 'revised_prompt': prompt})
                except Exception:
                    pass
        # Fallback: AI Horde (free, community-run, no auth)
        horde = requests.post(
            'https://aihorde.net/api/v2/generate/async',
            json={'prompt': prompt, 'params': {'width': 512, 'height': 512, 'steps': 20, 'n': 1},
                  'models': ['stable_diffusion']},
            headers={'apikey': '0000000000', 'Content-Type': 'application/json'},
            timeout=15
        )
        horde.raise_for_status()
        job_id = horde.json()['id']
        for _ in range(60):
            time.sleep(2)
            chk = requests.get(f'https://aihorde.net/api/v2/generate/check/{job_id}',
                               headers={'apikey': '0000000000'}, timeout=10)
            if chk.json().get('done'):
                status = requests.get(f'https://aihorde.net/api/v2/generate/status/{job_id}',
                                      headers={'apikey': '0000000000'}, timeout=10)
                img_b64 = status.json()['generations'][0]['img']
                if img_b64.startswith('http'):
                    img_r = requests.get(img_b64, timeout=15)
                    img_b64 = base64.b64encode(img_r.content).decode()
                return jsonify({'url': f'data:image/webp;base64,{img_b64}', 'revised_prompt': prompt})
        raise Exception('AI Horde timed out')
    except Exception as e:
        return jsonify({'error': _safe_err(e)}), 500


@app.route('/api/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url', '')
    try:
        r = requests.get(url, timeout=8,
                         headers={'User-Agent': 'Mozilla/5.0 (compatible; BAME-AI-Scraper/1.0)'})
        r.raise_for_status()
        return jsonify({'contents': r.text})
    except Exception as e:
        return jsonify({'error': _safe_err(e), 'contents': ''})


@app.route('/api/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    try:
        r = requests.get(
            f'https://html.duckduckgo.com/html/?q={requests.utils.quote(query)}',
            timeout=7,
            headers={'User-Agent': 'Mozilla/5.0 (compatible; BAME-AI-Search/1.0)'}
        )
        return jsonify({'contents': r.text})
    except Exception as e:
        return jsonify({'error': _safe_err(e), 'contents': ''})


CHAT_MODELS = ['gemini-2.5-flash-lite', 'gemini-2.0-flash-lite', 'gemini-2.0-flash', 'gemini-flash-latest']

def _call_google(messages, system):
    contents = [
        {'role': 'model' if m['role'] == 'assistant' else 'user', 'parts': [{'text': m['content']}]}
        for m in messages
    ]
    last_err = None
    for model in CHAT_MODELS:
        for key in GOOGLE_API_KEYS:
            try:
                r = requests.post(
                    f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}',
                    json={'system_instruction': {'parts': [{'text': system}]}, 'contents': contents,
                          'generationConfig': {'maxOutputTokens': 8192}},
                    timeout=30
                )
                r.raise_for_status()
                return r.json()['candidates'][0]['content']['parts'][0]['text']
            except Exception as e:
                last_err = e
    raise last_err


def _stream_google(messages, system):
    contents = [
        {'role': 'model' if m['role'] == 'assistant' else 'user', 'parts': [{'text': m['content']}]}
        for m in messages
    ]
    last_err = None
    for model in CHAT_MODELS:
        for key in GOOGLE_API_KEYS:
            try:
                with requests.post(
                    f'https://generativelanguage.googleapis.com/v1beta/models/{model}:streamGenerateContent?alt=sse&key={key}',
                    json={'system_instruction': {'parts': [{'text': system}]}, 'contents': contents,
                          'generationConfig': {'maxOutputTokens': 8192}},
                    stream=True, timeout=60
                ) as r:
                    r.raise_for_status()
                    for line in r.iter_lines():
                        if line:
                            decoded = line.decode('utf-8')
                            if decoded.startswith('data:'):
                                try:
                                    d = json.loads(decoded[5:].strip())
                                    text = d.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
                                    if text:
                                        yield f"data: {json.dumps({'text': text})}\n\n"
                                except Exception:
                                    pass
                    return  # success
            except Exception as e:
                last_err = e
    raise last_err


if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
