---
layout: post 
title: I'm Rishab Shyamal
hide: true
---

Hi! My name is Rishab Shyamal 

### Development Environment

> Coding starts with tools, explore these tools and procedures with a click.

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
    <a href="https://github.com/Open-Coding-Society/student">
        <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
    </a>
    <a href="https://open-coding-society.github.io/student">
        <img src="https://img.shields.io/badge/GitHub%20Pages-327FC7?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Pages">
    </a>
    <a href="https://kasm.opencodingsociety.com/">
        <img src="https://img.shields.io/badge/KASM-0078D4?style=for-the-badge&logo=kasm&logoColor=white" alt="KASM">
    </a>
    <a href="https://vscode.dev/">
        <img src="https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VSCode">
    </a>
</div>

<!-- Fun Fact Generator -->
<div id="fun-fact-widget" style="margin-top: 18px; padding: 16px; border-radius: 8px; background: #000; color: #fff; box-shadow: 0 2px 6px rgba(0,0,0,0.45); max-width:720px;">
    <h4 style="margin:0 0 8px 0; color: #fff;">Fun Fact Generator</h4>
    <p id="fun-fact-text" style="margin:0 0 12px 0; font-size:1.05rem; color: #ddd;">Click the button to reveal a random fun fact — powered by the web with a local fallback.</p>
    <div style="display:flex; gap:10px; align-items:center;">
        <button id="fun-fact-btn" style="background:#327FC7;color:#fff;border:none;padding:8px 14px;border-radius:6px;cursor:pointer;font-weight:600;">Get a Fun Fact</button>
        <button id="fun-fact-copy" style="background:#222;color:#fff;border:none;padding:8px 10px;border-radius:6px;cursor:pointer;">Copy</button>
        <small id="fun-fact-source" style="color:#bbb; margin-left:8px;">source: web / fallback</small>
    </div>
</div>

<script>
    (function(){
        const localFacts = [
            "Honey never spoils — edible honey was found in ancient Egyptian tombs.",
            "Octopuses have three hearts and blue blood.",
            "A group of flamingos is called a flamboyance.",
            "Bananas are berries — but strawberries aren't.",
            "Wombat poop is cube-shaped, which helps it not to roll away.",
            "There are more possible iterations of a game of chess than atoms in the known universe (roughly).",
            "The Eiffel Tower can be 15 cm taller during the summer from thermal expansion.",
            "A day on Venus is longer than a year on Venus.",
            "Sloths can hold their breath for up to 40 minutes by slowing their heart rate.",
            "The first computer bug was an actual moth trapped in a relay."
        ];

        const factBtn = document.getElementById('fun-fact-btn');
        const factText = document.getElementById('fun-fact-text');
        const factSource = document.getElementById('fun-fact-source');
        const copyBtn = document.getElementById('fun-fact-copy');

        function showFact(text, sourceLabel){
            factText.textContent = text;
            factSource.textContent = `source: ${sourceLabel}`;
        }

        async function fetchWebFact(){
            try{
                // Try a public random fact API first
                const res = await fetch('https://uselessfacts.jsph.pl/random.json?language=en');
                if(!res.ok) throw new Error('network');
                const data = await res.json();
                if(data && data.text){
                    showFact(data.text, 'web');
                    return true;
                }
            }catch(e){
                return false;
            }
            return false;
        }

        async function getFact(){
            showFact('Fetching a fun fact...', '...');
            const ok = await fetchWebFact();
            if(!ok){
                // fallback to local facts
                const f = localFacts[Math.floor(Math.random()*localFacts.length)];
                showFact(f, 'local fallback');
            }
        }

        factBtn.addEventListener('click', getFact);

        copyBtn.addEventListener('click', function(){
            const text = factText.textContent || '';
            if(!text) return;
            if(navigator.clipboard && navigator.clipboard.writeText){
                navigator.clipboard.writeText(text).then(()=>{
                    copyBtn.textContent = 'Copied!';
                    setTimeout(()=> copyBtn.textContent = 'Copy',1200);
                });
            } else {
                // older fallback
                const ta = document.createElement('textarea');
                ta.value = text; document.body.appendChild(ta); ta.select();
                try{ document.execCommand('copy'); copyBtn.textContent='Copied!'; }
                catch(e){}
                document.body.removeChild(ta);
                setTimeout(()=> copyBtn.textContent = 'Copy',1200);
            }
        });

        // load one fact on page load
        if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', getFact);
        else getFact();
    })();
</script>


### Class Progress

> Here is my progress through coding, click to see these online - Some are games, some are blog posts, some are classworks/homeworks

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
    <a href="{{site.baseurl}}/snake" style="text-decoration: none;">
        <div style="background-color: #00FF00; color: black; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
            Snake Game
        </div>
    </a>
    <a href="{{site.baseurl}}/turtle" style="text-decoration: none;">
        <div style="background-color: #FF0000; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
            Turtle
        </div>
    </a>
    <a href="{{site.baseurl}}/calculator" style="text-decoration: none;">
        <div style="background-color: #1E90FF; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
            Calculator
        </div>
    </a>
    <a href="{{site.baseurl}}/custompong" style="text-decoration: none;">
        <div style="background-color: #FF8C00; color: black; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
            Pong
        </div>
    </a>
    <a href="{{site.baseurl}}/whos-that-pokemon" style="text-decoration: none;">
        <div style="background-color: #FFD700; color: black; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
            What's That Pokémon!
        </div>
    </a>
</div>

<br>

<!-- Contact Section -->
### Get in Touch

> Feel free to reach out if you'd like to collaborate or learn more about our work. I don't bite!
<p style="color: #2A7DB1;">My 🔥aura🔥 <a href="https://youtu.be/4uDgMx2V3Hc" style="color: #2A7DB1; text-decoration: underline;">video</a></p>

> Have a good day!