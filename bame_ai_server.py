import os
import json
import requests
from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', '')


@app.route('/api/providers')
def get_providers():
    return jsonify({'google': bool(GOOGLE_API_KEY)})


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    system = data.get('system', '')
    try:
        return jsonify({'content': _call_google(messages, system)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/stream', methods=['POST'])
def stream():
    data = request.json
    messages = data.get('messages', [])
    system = data.get('system', '')

    def generate():
        try:
            yield from _stream_google(messages, system)
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'}
    )


@app.route('/api/image', methods=['POST'])
def image():
    prompt = request.json.get('prompt', '')
    try:
        r = requests.post(
            f'https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:predict?key={GOOGLE_API_KEY}',
            json={'instances': [{'prompt': prompt}], 'parameters': {'sampleCount': 1}},
            timeout=60
        )
        r.raise_for_status()
        b64 = r.json()['predictions'][0]['bytesBase64Encoded']
        return jsonify({'url': f'data:image/png;base64,{b64}', 'revised_prompt': prompt})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url', '')
    try:
        r = requests.get(url, timeout=8,
                         headers={'User-Agent': 'Mozilla/5.0 (compatible; BAME-AI-Scraper/1.0)'})
        r.raise_for_status()
        return jsonify({'contents': r.text})
    except Exception as e:
        return jsonify({'error': str(e), 'contents': ''})


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
        return jsonify({'error': str(e), 'contents': ''})


def _call_google(messages, system):
    contents = [
        {'role': 'model' if m['role'] == 'assistant' else 'user', 'parts': [{'text': m['content']}]}
        for m in messages
    ]
    r = requests.post(
        f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key={GOOGLE_API_KEY}',
        json={'system_instruction': {'parts': [{'text': system}]}, 'contents': contents,
              'generationConfig': {'maxOutputTokens': 8192}},
        timeout=30
    )
    r.raise_for_status()
    return r.json()['candidates'][0]['content']['parts'][0]['text']


def _stream_google(messages, system):
    contents = [
        {'role': 'model' if m['role'] == 'assistant' else 'user', 'parts': [{'text': m['content']}]}
        for m in messages
    ]
    with requests.post(
        f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:streamGenerateContent?alt=sse&key={GOOGLE_API_KEY}',
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


if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
