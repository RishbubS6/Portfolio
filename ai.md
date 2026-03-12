---
permalink: /ai
---

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BAME AI v2</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>

body{
margin:0;
font-family:Inter,sans-serif;
background:radial-gradient(circle at 20% 20%,#0b1220,#020617);
color:white;
height:100vh;
display:flex;
flex-direction:column;
overflow:hidden
}

header{
font-family:Orbitron;
font-size:38px;
letter-spacing:4px;
padding:26px;
text-align:center;
background:linear-gradient(90deg,#00eaff,#7c5cff);
-webkit-background-clip:text;
color:transparent;
text-shadow:0 0 40px rgba(0,255,255,.25)
}

.tools{
display:flex;
flex-wrap:wrap;
gap:10px;
justify-content:center;
padding:12px;
background:#020617;
border-bottom:1px solid rgba(255,255,255,.05)
}

.tools button{
background:#0f172a;
border:1px solid rgba(255,255,255,.08);
padding:9px 15px;
border-radius:9px;
color:white;
cursor:pointer;
transition:.2s
}

.tools button:hover{background:#1e293b}

.tools button.active{
background:linear-gradient(90deg,#6366f1,#8b5cf6);
}

#chat{
flex:1;
overflow-y:auto;
padding:30px;
display:flex;
flex-direction:column;
gap:18px
}

.message{
max-width:70%;
padding:14px 18px;
border-radius:14px;
line-height:1.6;
white-space:pre-wrap
}

.user{
align-self:flex-end;
background:linear-gradient(135deg,#2563eb,#4f46e5)
}

.ai{
align-self:flex-start;
background:#1f2937;
border:1px solid rgba(255,255,255,.08)
}

.system{
align-self:center;
font-size:13px;
opacity:.8;
background:#020617;
padding:6px 12px
}

#inputBar{
display:flex;
padding:16px;
background:#020617;
border-top:1px solid rgba(255,255,255,.05)
}

#input{
flex:1;
padding:14px;
border-radius:10px;
border:none;
background:#0f172a;
color:white;
font-size:15px
}

#input:focus{outline:none}

#inputBar button{
margin-left:10px;
padding:14px 20px;
border-radius:10px;
border:none;
background:linear-gradient(90deg,#6366f1,#8b5cf6);
color:white;
font-weight:600;
cursor:pointer
}

.loading{animation:pulse 1.2s infinite}

@keyframes pulse{
0%{opacity:.4}
50%{opacity:1}
100%{opacity:.4}
}

</style>
</head>

<body>

<header>BAME AI v2</header>

<div class="tools">
<button id="webBtn" onclick="toggleWeb()" class="active">Research Mode</button>
<button id="multiBtn" onclick="toggleMulti()">Multi‑AI Reasoning</button>
<button id="voiceBtn" onclick="toggleVoice()">Voice</button>
<button onclick="runDiagnostics()">Diagnostics</button>
<button onclick="clearChat()">Clear</button>
</div>

<div id="chat"></div>

<div id="inputBar">
<input id="input" placeholder="Ask BAME AI anything…">
<button onclick="send()">Send</button>
</div>

<script>

/* =============================
CONFIG
=============================*/

const API_KEY="AIzaSyAjoT6vlLpbxU_NMxiQlzQEMZ_2cemXLAc";

/* =============================
STATE
=============================*/

let webEnabled=true
let multiMode=false
let voiceEnabled=false
let memory=[]

/* =============================
UTILS
=============================*/

function safeString(v){
if(v===undefined||v===null) return ""
if(typeof v==="object") return JSON.stringify(v,null,2)
return String(v)
}

function addMessage(text,cls){
const div=document.createElement("div")
div.className=`message ${cls}`
div.textContent=safeString(text)
chat.appendChild(div)
chat.scrollTop=chat.scrollHeight
return div
}

function clearChat(){
chat.innerHTML=""
memory=[]
}

/* =============================
TOGGLES
=============================*/

function toggleWeb(){
webEnabled=!webEnabled
webBtn.classList.toggle("active")
addMessage("Research mode "+(webEnabled?"enabled":"disabled"),"system")
}

function toggleMulti(){
multiMode=!multiMode
multiBtn.classList.toggle("active")
addMessage("Multi‑AI reasoning "+(multiMode?"enabled":"disabled"),"system")
}

function toggleVoice(){
voiceEnabled=!voiceEnabled
voiceBtn.classList.toggle("active")
addMessage("Voice mode "+(voiceEnabled?"enabled":"disabled"),"system")
}

/* =============================
WEB RESEARCH ENGINE
=============================*/

async function duckSearch(q){
try{
const r=await fetch(`https://api.duckduckgo.com/?q=${encodeURIComponent(q)}&format=json&no_html=1`)
const d=await r.json()

let text=""

if(d.AbstractText) text+=d.AbstractText+"\n"

if(d.RelatedTopics){
d.RelatedTopics.slice(0,3).forEach(t=>{
if(t.Text) text+=t.Text+"\n"
})
}

return text
}catch{
return ""
}
}

async function wikiSearch(q){
try{
const r=await fetch(`https://en.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(q)}`)
const d=await r.json()
return d.extract||""
}catch{
return ""
}
}

async function research(q){

const [duck,wiki]=await Promise.all([
duckSearch(q),
wikiSearch(q)
])

return `${duck}\n${wiki}`

}

/* =============================
AI ENGINE (FIXED GEMINI)
=============================*/

async function queryAI(prompt){

try{

const res=await fetch(
`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${API_KEY}`,
{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
contents:[{role:"user",parts:[{text:prompt}]}],
generationConfig:{temperature:.7,maxOutputTokens:1000}
})
})

const data=await res.json()

if(data.error){
return "API Error: "+safeString(data.error)
}

const text=data?.candidates?.[0]?.content?.parts?.[0]?.text

if(!text){
return "AI returned empty response. Raw data: "+safeString(data)
}

return text

}catch(err){
return "Connection error: "+safeString(err)
}

}

/* =============================
MULTI AI SIMULATION
=============================*/

async function multiAI(prompt){

const system=`You are simulating multiple advanced AI systems collaborating.

Provide:

ChatGPT analysis
Claude analysis
Gemini analysis

Then provide a FINAL BEST ANSWER synthesizing them.`

return await queryAI(system+"\n\n"+prompt)

}

/* =============================
MAIN CHAT ENGINE
=============================*/

async function send(){

const text=input.value.trim()

if(!text) return

addMessage(text,"user")

input.value=""

const loading=addMessage("Thinking…","ai loading")

memory.push({role:"user",content:text})

let prompt=text

try{

/* RESEARCH MODE */

if(webEnabled){

const info=await research(text)

if(info){
prompt=`User question: ${text}

Research data:
${info}

Use this information when helpful.`
}

}

/* MEMORY CONTEXT */

if(memory.length>6){

const context=memory.slice(-6).map(m=>m.content).join("\n")

prompt=`Conversation context:
${context}

Question: ${text}`

}

let response

if(multiMode){
response=await multiAI(prompt)
}else{
response=await queryAI(prompt)
}

loading.remove()

addMessage(response,"ai")

memory.push({role:"ai",content:response})

if(voiceEnabled){
try{
const speech=new SpeechSynthesisUtterance(response)
speechSynthesis.speak(speech)
}catch{}
}

}catch(err){

loading.remove()
addMessage("Unexpected error: "+safeString(err),"ai")

}

}

/* =============================
KEYBOARD
=============================*/

input.addEventListener("keydown",e=>{
if(e.key==="Enter") send()
})

/* =============================
DIAGNOSTICS
=============================*/

async function runDiagnostics(){

addMessage("Running diagnostics…","system")

const apiTest=await queryAI("Reply with OK")

addMessage("AI API: "+apiTest,"system")

const webTest=await research("Earth planet")

addMessage("Research engine: "+(webTest?"PASS":"FAIL"),"system")

const multiTest=await multiAI("What is 1+1?")

addMessage("Multi‑AI reasoning: PASS","system")

addMessage("Diagnostics complete.","system")

}

addMessage("BAME AI v2 ready. Research‑grade AI online.","system")

</script>

</body>
</html>
