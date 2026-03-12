---
permalink: /ai
---


<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/9.1.6/marked.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
:root{
  --bg:#07080f;--surface:#0d0f1c;--surface2:#131628;--surface3:#1a1e34;
  --border:rgba(99,102,241,0.12);--border-hi:rgba(99,102,241,0.35);
  --accent:#6366f1;--accent-h:#818cf8;--accent2:#06b6d4;--accent3:#a78bfa;
  --glow:rgba(99,102,241,0.25);--text:#e2e4f0;--muted:#6b7280;--muted2:#374151;
  --danger:#ef4444;--ok:#10b981;--warn:#f59e0b;
}
html,body{height:100%;overflow:hidden;}
.site-header{transform:translateY(-100%);}
body{font-family:'Syne',sans-serif;background:var(--bg);color:var(--text);display:flex;flex-direction:column;}
body::after{content:'';position:fixed;inset:0;pointer-events:none;z-index:0;opacity:0.022;background-image:linear-gradient(var(--accent) 1px,transparent 1px),linear-gradient(90deg,var(--accent) 1px,transparent 1px);background-size:40px 40px;}
body::before{content:'';position:fixed;inset:0;pointer-events:none;z-index:9999;opacity:0.25;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");}

/* ══ ONBOARDING ══ */
#onboarding{position:fixed;inset:0;background:var(--bg);display:flex;align-items:flex-start;justify-content:center;z-index:1000;padding:40px 24px 60px;overflow-y:auto;transition:opacity .5s,transform .5s;}
#onboarding.hidden{opacity:0;transform:scale(.96);pointer-events:none;}
.ob-inner{max-width:600px;width:100%;margin:auto;animation:riseIn .7s cubic-bezier(.16,1,.3,1) both;position:relative;z-index:1;}
@keyframes riseIn{from{opacity:0;transform:translateY(30px);}to{opacity:1;transform:translateY(0);}}
.ob-logo{display:flex;align-items:center;gap:20px;margin-bottom:44px;}
.ob-icon{width:64px;height:64px;border-radius:16px;background:linear-gradient(135deg,var(--accent),var(--accent3));display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:900;color:#fff;box-shadow:0 0 32px var(--glow),0 0 8px rgba(99,102,241,.5);flex-shrink:0;}
.ob-title-text{font-size:clamp(36px,6vw,56px);font-weight:800;line-height:1;letter-spacing:-2px;}
.ob-title-text span{background:linear-gradient(135deg,var(--accent),var(--accent3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.ob-sub{font-size:13px;color:var(--muted);margin-top:7px;font-family:'JetBrains Mono',monospace;font-weight:300;letter-spacing:.08em;}
.ob-divider{width:100%;height:1px;background:var(--border-hi);margin:28px 0;}
.ob-label{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:14px;font-family:'JetBrains Mono',monospace;}
.tone-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:28px;}
.tone-card{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:16px 18px;cursor:pointer;transition:all .2s;position:relative;overflow:hidden;user-select:none;}
.tone-card::after{content:'';position:absolute;inset:0;background:var(--accent);opacity:0;transition:opacity .2s;}
.tone-card:hover{border-color:var(--border-hi);transform:translateY(-2px);box-shadow:0 4px 20px rgba(99,102,241,.12);}
.tone-card.selected{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent),0 4px 24px rgba(99,102,241,.2);}
.tone-card.selected::after{opacity:.06;}
.tone-emoji{font-size:24px;margin-bottom:6px;display:block;position:relative;z-index:1;}
.tone-name{font-size:13px;font-weight:700;margin-bottom:3px;position:relative;z-index:1;}
.tone-desc{font-size:10px;color:var(--muted);font-family:'JetBrains Mono',monospace;font-weight:300;line-height:1.5;position:relative;z-index:1;}
.tone-card.selected .tone-name{color:var(--accent-h);}
.prov-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:20px;}
.prov-card{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:14px 12px;cursor:pointer;transition:all .2s;text-align:center;user-select:none;}
.prov-card:hover{border-color:var(--border-hi);transform:translateY(-1px);}
.prov-card.selected{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent),0 4px 20px rgba(99,102,241,.18);}
.prov-logo{font-size:22px;margin-bottom:6px;display:block;}
.prov-name{font-size:12px;font-weight:700;}
.prov-model{font-size:10px;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-top:2px;}
.prov-card.selected .prov-name{color:var(--accent-h);}
.api-row{display:flex;flex-direction:column;gap:10px;margin-bottom:28px;}
.api-wrap{position:relative;display:flex;align-items:center;}
.api-input{width:100%;background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:14px 48px 14px 16px;color:var(--text);font-family:'JetBrains Mono',monospace;font-size:13px;outline:none;transition:all .2s;}
.api-input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(99,102,241,.12);}
.api-input::placeholder{color:var(--muted2);}
.api-eye{position:absolute;right:14px;background:none;border:none;color:var(--muted);cursor:pointer;font-size:16px;padding:4px;transition:color .2s;line-height:1;}
.api-eye:hover{color:var(--text);}
.api-hint{font-size:11px;color:var(--muted);font-family:'JetBrains Mono',monospace;line-height:1.65;}
.api-hint a{color:var(--accent-h);text-decoration:none;}
.api-hint a:hover{text-decoration:underline;}
.ob-btn{width:100%;padding:16px;border:none;border-radius:10px;background:linear-gradient(135deg,var(--accent),var(--accent3));color:#fff;font-family:'Syne',sans-serif;font-size:15px;font-weight:700;cursor:pointer;letter-spacing:.06em;transition:all .2s;text-transform:uppercase;}
.ob-btn:hover{opacity:.9;transform:translateY(-1px);box-shadow:0 8px 30px rgba(99,102,241,.4);}

/* ══ APP SHELL ══ */
#app{display:flex;flex-direction:column;height:100vh;opacity:0;transition:opacity .5s;pointer-events:none;position:fixed;inset:0;z-index:1;}
#app.visible{opacity:1;pointer-events:all;}
header{display:flex;align-items:center;justify-content:space-between;padding:9px 14px;border-bottom:1px solid var(--border);background:rgba(13,15,28,.97);backdrop-filter:blur(12px);flex-shrink:0;gap:8px;z-index:10;position:relative;}
.h-left{display:flex;align-items:center;gap:10px;flex-shrink:0;}
.h-icon{width:27px;height:27px;border-radius:7px;background:linear-gradient(135deg,var(--accent),var(--accent3));display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:900;color:#fff;box-shadow:0 0 10px rgba(99,102,241,.4);}
.h-title{font-size:15px;font-weight:800;letter-spacing:-.5px;white-space:nowrap;}
.h-title span{background:linear-gradient(135deg,var(--accent),var(--accent3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.h-badge{font-family:'JetBrains Mono',monospace;font-size:9px;background:var(--surface3);border:1px solid var(--border-hi);color:var(--accent-h);padding:2px 8px;border-radius:20px;letter-spacing:.1em;text-transform:uppercase;}
.h-right{display:flex;align-items:center;gap:5px;flex-wrap:wrap;}
.tone-pill{display:flex;align-items:center;gap:5px;background:var(--surface2);border:1px solid var(--border);border-radius:20px;padding:4px 10px;font-size:11px;color:var(--muted);cursor:pointer;transition:all .2s;font-family:'JetBrains Mono',monospace;white-space:nowrap;}
.tone-pill:hover{border-color:var(--border-hi);color:var(--text);}
.hbtn{background:var(--surface2);border:1px solid var(--border);border-radius:6px;padding:4px 9px;color:var(--muted);font-family:'Syne',sans-serif;font-size:10px;font-weight:600;cursor:pointer;transition:all .2s;letter-spacing:.04em;text-transform:uppercase;white-space:nowrap;}
.hbtn:hover{border-color:var(--border-hi);color:var(--text);}
.hbtn.danger:hover{border-color:var(--danger);color:var(--danger);}
.hbtn.active{border-color:var(--accent);color:var(--accent-h);background:rgba(99,102,241,.08);}

/* ══ CONVERSATION TABS ══ */
#conv-bar{display:flex;align-items:flex-end;gap:3px;padding:6px 14px 0;background:var(--surface);border-bottom:1px solid var(--border);flex-shrink:0;overflow-x:auto;}
#conv-bar::-webkit-scrollbar{height:3px;}
#conv-bar::-webkit-scrollbar-thumb{background:var(--surface3);}
.ctab{display:flex;align-items:center;gap:5px;padding:5px 10px 7px;border-radius:8px 8px 0 0;background:var(--surface2);border:1px solid var(--border);border-bottom:none;font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted);cursor:pointer;transition:all .15s;white-space:nowrap;min-width:70px;max-width:140px;}
.ctab.active{background:var(--bg);border-color:var(--border-hi);color:var(--text);}
.ctab-name{flex:1;overflow:hidden;text-overflow:ellipsis;min-width:0;}
.ctab-x{background:none;border:none;color:var(--muted);cursor:pointer;font-size:11px;padding:0;line-height:1;opacity:0;transition:opacity .15s;}
.ctab:hover .ctab-x{opacity:1;}
.ctab-x:hover{color:var(--danger);}
.ctab-new{background:none;border:1px dashed var(--border);border-radius:6px;padding:3px 8px;color:var(--muted);cursor:pointer;font-size:14px;transition:all .15s;flex-shrink:0;line-height:1.2;}
.ctab-new:hover{border-color:var(--border-hi);color:var(--text);}

/* ══ STATUS BAR ══ */
.status-bar{display:flex;align-items:center;gap:7px;padding:4px 14px;background:var(--surface);border-bottom:1px solid var(--border);flex-shrink:0;overflow:hidden;}
.sdot{width:6px;height:6px;border-radius:50%;background:var(--ok);flex-shrink:0;animation:pulseG 2.5s infinite;}
@keyframes pulseG{0%,100%{opacity:1;box-shadow:0 0 0 0 rgba(16,185,129,.4);}50%{opacity:.7;box-shadow:0 0 0 4px rgba(16,185,129,0);}}
.sdot.thinking{background:var(--accent);animation:pulseA .7s infinite;}
@keyframes pulseA{0%,100%{opacity:1;box-shadow:0 0 6px var(--accent);}50%{opacity:.4;box-shadow:none;}}
.stext{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted);flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.smodel{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted2);white-space:nowrap;flex-shrink:0;}

/* ══ LAYOUT ══ */
#layout{display:flex;flex:1;min-height:0;overflow:hidden;}
#chat-side{display:flex;flex-direction:column;flex:1;min-width:0;position:relative;}
#chat{flex:1;overflow-y:auto;padding:20px 14px;display:flex;flex-direction:column;gap:18px;min-height:0;}
#chat::-webkit-scrollbar{width:4px;}
#chat::-webkit-scrollbar-thumb{background:var(--surface3);border-radius:2px;}

/* ══ ARTIFACT PANEL ══ */
#art-panel{width:0;flex-shrink:0;border-left:1px solid var(--border);background:var(--surface);display:flex;flex-direction:column;overflow:hidden;transition:width .35s cubic-bezier(.16,1,.3,1);}
#art-panel.open{width:50%;}
.art-hdr{display:flex;align-items:center;gap:7px;padding:8px 11px;border-bottom:1px solid var(--border);flex-shrink:0;}
.art-title{font-size:11px;font-weight:700;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.art-lang{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--accent-h);background:var(--surface2);border:1px solid var(--border);padding:2px 7px;border-radius:10px;}
.art-tabs{display:flex;gap:2px;}
.atab{background:none;border:1px solid var(--border);border-radius:5px;padding:3px 8px;color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:9px;cursor:pointer;transition:all .15s;}
.atab.active{background:linear-gradient(135deg,var(--accent),var(--accent3));border-color:transparent;color:#fff;font-weight:700;}
.atab:hover:not(.active){border-color:var(--border-hi);color:var(--text);}
.art-btns{display:flex;gap:4px;}
.abtn{background:none;border:1px solid var(--border);border-radius:5px;padding:3px 6px;color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:9px;cursor:pointer;transition:all .15s;white-space:nowrap;}
.abtn:hover{border-color:var(--border-hi);color:var(--text);}
.art-close{background:none;border:none;color:var(--muted);cursor:pointer;font-size:15px;padding:2px 4px;transition:color .15s;line-height:1;}
.art-close:hover{color:var(--danger);}
#art-body{flex:1;overflow:hidden;position:relative;}
#art-iframe{width:100%;height:100%;border:none;background:#fff;display:block;}
#art-code{width:100%;height:100%;overflow:auto;display:none;}
#art-code::-webkit-scrollbar{width:4px;}
#art-code::-webkit-scrollbar-thumb{background:var(--surface3);border-radius:2px;}
#art-code pre{margin:0;min-height:100%;}
#art-code pre code{font-family:'JetBrains Mono',monospace!important;font-size:12px!important;line-height:1.6!important;padding:16px!important;display:block;background:#0d0e14!important;min-height:100%;}
.art-empty{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;gap:10px;color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:11px;}
.art-empty-icon{font-size:34px;opacity:.3;}

/* ══ MESSAGES ══ */
.msg{display:flex;gap:9px;max-width:840px;width:100%;animation:msgIn .3s cubic-bezier(.16,1,.3,1) both;}
@keyframes msgIn{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:translateY(0);}}
.msg.user{flex-direction:row-reverse;align-self:flex-end;}
.msg.ai{align-self:flex-start;}
.msg-av{width:29px;height:29px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:900;flex-shrink:0;margin-top:17px;}
.msg.ai .msg-av{background:linear-gradient(135deg,var(--accent),var(--accent3));color:#fff;box-shadow:0 0 10px rgba(99,102,241,.3);}
.msg.user .msg-av{background:var(--surface3);border:1px solid var(--border);font-size:13px;}
.msg-body{display:flex;flex-direction:column;gap:4px;min-width:0;flex:1;}
.msg.user .msg-body{align-items:flex-end;}
.msg-meta{display:flex;align-items:center;gap:6px;font-size:10px;color:var(--muted);font-family:'JetBrains Mono',monospace;}
.msg-bubble{padding:10px 13px;border-radius:12px;font-size:13.5px;line-height:1.75;max-width:680px;word-break:break-word;}
.msg.user .msg-bubble{background:var(--surface2);border:1px solid var(--border);border-top-right-radius:3px;}
.msg.ai .msg-bubble{background:var(--surface);border:1px solid var(--border);border-top-left-radius:3px;}
.stream-cur::after{content:'▋';animation:blink .6s infinite;color:var(--accent);}
@keyframes blink{0%,50%{opacity:1;}51%,100%{opacity:0;}}

/* source chips */
.sources-row{margin-top:8px;max-width:680px;}
.src-label{font-size:9px;color:var(--muted);font-family:'JetBrains Mono',monospace;letter-spacing:.1em;text-transform:uppercase;margin-bottom:5px;}
.src-chips{display:flex;flex-wrap:wrap;gap:5px;}
.src-chip{display:inline-flex;align-items:center;gap:4px;background:var(--surface2);border:1px solid var(--border-hi);border-radius:20px;padding:3px 9px;font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--accent2);cursor:pointer;text-decoration:none;transition:all .15s;max-width:220px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;}
.src-chip:hover{border-color:var(--accent2);background:rgba(6,182,212,.08);}

/* artifact pill */
.art-pill{display:inline-flex;align-items:center;gap:9px;background:var(--surface2);border:1px solid var(--border-hi);border-radius:10px;padding:8px 12px;margin-top:7px;cursor:pointer;transition:all .2s;max-width:360px;width:100%;}
.art-pill:hover{border-color:var(--accent);transform:translateY(-1px);box-shadow:0 4px 16px rgba(99,102,241,.15);}
.art-pill-ic{font-size:17px;flex-shrink:0;}
.art-pill-info{flex:1;min-width:0;}
.art-pill-title{font-size:11px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.art-pill-meta{font-size:9px;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-top:1px;}
.art-pill-arr{color:var(--accent-h);font-size:12px;flex-shrink:0;}

/* image gen result */
.img-result{margin-top:8px;background:var(--surface2);border:1px solid var(--border-hi);border-radius:12px;overflow:hidden;max-width:500px;}
.img-result-hdr{display:flex;align-items:center;gap:8px;padding:7px 11px;border-bottom:1px solid var(--border);font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--accent3);}
.gen-img{width:100%;display:block;}
.img-result-btns{display:flex;gap:5px;padding:7px 11px;border-top:1px solid var(--border);}
.img-abtn{background:var(--surface3);border:1px solid var(--border);border-radius:6px;padding:4px 8px;color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:9px;cursor:pointer;transition:all .15s;text-decoration:none;display:inline-flex;align-items:center;gap:3px;}
.img-abtn:hover{border-color:var(--border-hi);color:var(--text);}

/* file attachments */
.attach-strip{display:flex;flex-wrap:wrap;gap:6px;padding:0 0 6px;}
.atch{display:inline-flex;align-items:center;gap:6px;background:var(--surface2);border:1px solid var(--border-hi);border-radius:7px;padding:5px 9px;font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text);}
.atch-ic{font-size:14px;}
.atch-name{max-width:130px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.atch-sz{color:var(--muted);font-size:9px;}
.atch-rm{background:none;border:none;color:var(--muted);cursor:pointer;font-size:13px;padding:0 0 0 3px;line-height:1;transition:color .15s;}
.atch-rm:hover{color:var(--danger);}
.msg-img{max-width:280px;border-radius:9px;margin-top:5px;border:1px solid var(--border);}

/* agent steps */
.agent-log{display:flex;flex-direction:column;gap:3px;margin-bottom:6px;max-width:680px;}
.agent-step{display:flex;align-items:center;gap:7px;padding:4px 9px;background:rgba(99,102,241,.05);border:1px solid rgba(99,102,241,.12);border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted);}
.agent-step.done{border-color:rgba(16,185,129,.2);background:rgba(16,185,129,.04);color:var(--ok);}
.agent-step.active{border-color:rgba(99,102,241,.3);background:rgba(99,102,241,.08);color:var(--accent-h);}

/* markdown */
.msg-bubble h1,.msg-bubble h2,.msg-bubble h3{font-family:'Syne',sans-serif;font-weight:700;margin:13px 0 5px;color:var(--accent-h);line-height:1.25;}
.msg-bubble h1{font-size:18px;}.msg-bubble h2{font-size:15px;}.msg-bubble h3{font-size:13px;}
.msg-bubble h1:first-child,.msg-bubble h2:first-child,.msg-bubble h3:first-child{margin-top:0;}
.msg-bubble p{margin-bottom:9px;}.msg-bubble p:last-child{margin-bottom:0;}
.msg-bubble ul,.msg-bubble ol{margin:5px 0 9px 18px;}.msg-bubble li{margin-bottom:3px;}
.msg-bubble strong{color:var(--accent-h);font-weight:700;}.msg-bubble em{color:var(--accent3);}
.msg-bubble a{color:var(--accent2);text-decoration:underline;}
.msg-bubble blockquote{border-left:3px solid var(--accent);padding:7px 12px;margin:8px 0;background:var(--surface2);border-radius:0 7px 7px 0;color:var(--muted);font-style:italic;}
.msg-bubble table{width:100%;border-collapse:collapse;margin:9px 0;font-size:12px;}
.msg-bubble th{background:var(--surface2);color:var(--accent-h);padding:6px 9px;text-align:left;border:1px solid var(--border);font-weight:600;font-family:'JetBrains Mono',monospace;font-size:9px;text-transform:uppercase;letter-spacing:.07em;}
.msg-bubble td{padding:6px 9px;border:1px solid var(--border);}
.msg-bubble tr:nth-child(even) td{background:var(--surface2);}
.msg-bubble pre{margin:8px 0;border-radius:9px;overflow:hidden;border:1px solid var(--border);}
.code-hdr{display:flex;align-items:center;justify-content:space-between;padding:5px 10px;background:#0d0e14;border-bottom:1px solid rgba(99,102,241,.1);}
.code-lang{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);text-transform:uppercase;letter-spacing:.1em;}
.copy-btn{background:none;border:1px solid rgba(99,102,241,.2);border-radius:4px;color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:9px;padding:2px 7px;cursor:pointer;transition:all .2s;}
.copy-btn:hover{border-color:var(--accent);color:var(--accent-h);}
.copy-btn.copied{color:var(--ok);border-color:var(--ok);}
.msg-bubble pre code{font-family:'JetBrains Mono',monospace!important;font-size:12px!important;line-height:1.6!important;display:block;padding:11px!important;background:#0d0e14!important;overflow-x:auto;}
.msg-bubble code:not(pre code){font-family:'JetBrains Mono',monospace;font-size:11px;background:var(--surface2);border:1px solid var(--border);padding:1px 5px;border-radius:4px;color:var(--accent2);}
.search-tag{display:inline-flex;align-items:center;gap:4px;background:rgba(6,182,212,.08);border:1px solid rgba(6,182,212,.22);border-radius:20px;padding:2px 9px;font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--accent2);margin-bottom:7px;}
.thinking-bubble{display:flex;align-items:center;gap:9px;color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:12px;}
.dots{display:flex;gap:4px;}
.dots span{width:5px;height:5px;border-radius:50%;background:var(--accent);animation:bounce 1.2s infinite;}
.dots span:nth-child(2){animation-delay:.2s;}.dots span:nth-child(3){animation-delay:.4s;}
@keyframes bounce{0%,60%,100%{transform:translateY(0);}30%{transform:translateY(-6px);}}
.msg-actions{display:flex;gap:5px;margin-top:3px;opacity:0;transition:opacity .2s;}
.msg:hover .msg-actions{opacity:1;}
.act-btn{background:var(--surface2);border:1px solid var(--border);border-radius:5px;padding:3px 7px;color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:9px;cursor:pointer;transition:all .2s;}
.act-btn:hover{border-color:var(--border-hi);color:var(--text);}

/* ══ WELCOME ══ */
#welcome{display:flex;flex-direction:column;align-items:center;justify-content:center;flex:1;gap:20px;text-align:center;padding:28px;min-height:300px;}
.wlc-logo{width:66px;height:66px;border-radius:18px;background:linear-gradient(135deg,var(--accent),var(--accent3));display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:900;color:#fff;box-shadow:0 0 36px rgba(99,102,241,.35);}
.wlc-title{font-size:clamp(20px,4vw,32px);font-weight:800;letter-spacing:-1px;line-height:1.1;}
.wlc-title span{background:linear-gradient(135deg,var(--accent),var(--accent3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.wlc-sub{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);max-width:400px;line-height:1.75;}
.cap-chips{display:flex;flex-wrap:wrap;gap:5px;justify-content:center;max-width:500px;}
.cap-chip{display:inline-flex;align-items:center;gap:4px;background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:3px 10px;font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);}
.starters{display:grid;grid-template-columns:repeat(2,1fr);gap:7px;max-width:520px;width:100%;}
.starter{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:10px 12px;text-align:left;cursor:pointer;transition:all .2s;font-size:11px;line-height:1.5;color:var(--muted);}
.starter:hover{border-color:var(--accent);color:var(--text);transform:translateY(-2px);box-shadow:0 4px 14px rgba(99,102,241,.1);}
.starter-ic{font-size:15px;margin-bottom:3px;display:block;}

/* ══ INPUT ══ */
.input-area{padding:10px 14px 14px;background:var(--surface);border-top:1px solid var(--border);flex-shrink:0;}
.input-wrap{max-width:840px;margin:0 auto;}
#attach-strip{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:6px;}
.input-row{display:flex;align-items:flex-end;gap:7px;background:var(--surface2);border:1px solid var(--border);border-radius:11px;padding:8px 10px;transition:border-color .2s,box-shadow .2s;}
.input-row:focus-within{border-color:var(--accent);box-shadow:0 0 0 3px rgba(99,102,241,.1);}
#userInput{flex:1;background:none;border:none;outline:none;color:var(--text);font-family:'Syne',sans-serif;font-size:13.5px;line-height:1.6;resize:none;max-height:140px;min-height:22px;overflow-y:auto;}
#userInput::placeholder{color:var(--muted2);}
.input-tools{display:flex;align-items:center;gap:4px;flex-shrink:0;}
.tbtn{background:none;border:1px solid var(--border);border-radius:6px;padding:4px 7px;color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:11px;cursor:pointer;transition:all .2s;white-space:nowrap;line-height:1;}
.tbtn:hover{border-color:var(--border-hi);color:var(--text);}
.tbtn.on{border-color:var(--accent2);color:var(--accent2);background:rgba(6,182,212,.08);}
.tbtn.rec{border-color:var(--danger);color:var(--danger);animation:voicePulse 1s infinite;}
@keyframes voicePulse{0%,100%{box-shadow:0 0 0 0 rgba(239,68,68,.4);}50%{box-shadow:0 0 0 5px rgba(239,68,68,0);}}
.send-btn{background:linear-gradient(135deg,var(--accent),var(--accent3));border:none;border-radius:8px;width:34px;height:34px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;flex-shrink:0;color:#fff;box-shadow:0 2px 10px rgba(99,102,241,.3);}
.send-btn:hover{opacity:.9;transform:scale(1.05);}
.send-btn:active{transform:scale(.96);}
.send-btn:disabled{opacity:.2;cursor:not-allowed;transform:none;box-shadow:none;}
.send-btn svg{width:14px;height:14px;}
.input-footer{display:flex;align-items:center;justify-content:space-between;margin-top:5px;padding:0 2px;}
.input-hint{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted2);}
.char-count{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted2);}
.char-count.warn{color:var(--warn);}
.char-count.crit{color:var(--danger);}

/* scroll btn */
#scroll-btn{position:absolute;bottom:90px;right:14px;background:var(--surface2);border:1px solid var(--border-hi);border-radius:50%;width:30px;height:30px;display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--muted);font-size:12px;transition:all .2s;opacity:0;pointer-events:none;z-index:50;}
#scroll-btn.show{opacity:1;pointer-events:all;}
#scroll-btn:hover{border-color:var(--accent);color:var(--accent-h);}

/* ══ MODALS (shared) ══ */
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.82);backdrop-filter:blur(12px);display:flex;align-items:center;justify-content:center;z-index:500;opacity:0;pointer-events:none;transition:opacity .25s;padding:20px;}
.overlay.open{opacity:1;pointer-events:all;}
.mbox{background:var(--surface);border:1px solid var(--border-hi);border-radius:16px;padding:24px;max-width:480px;width:100%;animation:mIn .3s cubic-bezier(.16,1,.3,1) both;box-shadow:0 20px 60px rgba(0,0,0,.5);max-height:90vh;overflow-y:auto;}
.mbox::-webkit-scrollbar{width:3px;}
.mbox::-webkit-scrollbar-thumb{background:var(--surface3);}
@keyframes mIn{from{transform:scale(.93) translateY(12px);}to{transform:scale(1) translateY(0);}}
.mtitle{font-size:17px;font-weight:700;margin-bottom:14px;}
.mlabel{font-size:9px;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-bottom:7px;display:block;}
.mactions{display:flex;gap:9px;margin-top:14px;}
.mbtn{flex:1;padding:10px;border-radius:8px;font-family:'Syne',sans-serif;font-size:11px;font-weight:700;cursor:pointer;transition:all .2s;letter-spacing:.04em;text-transform:uppercase;}
.mbtn.cancel{background:var(--surface2);border:1px solid var(--border);color:var(--muted);}
.mbtn.cancel:hover{border-color:var(--border-hi);color:var(--text);}
.mbtn.ok{background:linear-gradient(135deg,var(--accent),var(--accent3));border:none;color:#fff;}
.mbtn.ok:hover{opacity:.9;}
.mbtn.go{background:linear-gradient(135deg,var(--ok),#0a9a6e);border:none;color:#fff;}
.mbtn.go:hover{opacity:.9;}
.minput{width:100%;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:11px 13px;color:var(--text);font-family:'Syne',sans-serif;font-size:13px;outline:none;transition:all .2s;margin-bottom:10px;}
.minput:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(99,102,241,.12);}
.minput::placeholder{color:var(--muted2);}
.mcode{width:100%;min-height:150px;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:11px;color:var(--text);font-family:'JetBrains Mono',monospace;font-size:12px;outline:none;resize:vertical;transition:border-color .2s;}
.mcode:focus{border-color:var(--accent);}
.mout{background:#0d0e14;border:1px solid var(--border);border-radius:8px;padding:11px;font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--ok);min-height:70px;max-height:200px;overflow-y:auto;white-space:pre-wrap;margin-top:9px;}
.mout.err{color:var(--danger);}

/* depth / size / style pickers */
.picker-row{display:flex;gap:7px;margin-bottom:12px;}
.picker-btn{flex:1;padding:8px 6px;border-radius:7px;background:var(--surface2);border:1px solid var(--border);color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:9px;cursor:pointer;transition:all .15s;text-align:center;}
.picker-btn.sel{border-color:var(--accent);color:var(--accent-h);background:rgba(99,102,241,.08);}
.picker-btn:hover:not(.sel){border-color:var(--border-hi);color:var(--text);}
.chips-wrap{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:12px;}
.chip{background:var(--surface2);border:1px solid var(--border);border-radius:20px;padding:3px 9px;font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted);cursor:pointer;transition:all .15s;}
.chip.sel{border-color:var(--accent3);color:var(--accent3);background:rgba(167,139,250,.08);}
.chip:hover:not(.sel){border-color:var(--border-hi);color:var(--text);}

/* settings */
.skey-wrap{position:relative;display:flex;align-items:center;margin-bottom:6px;}
.skey-in{width:100%;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:11px 40px 11px 12px;color:var(--text);font-family:'JetBrains Mono',monospace;font-size:12px;outline:none;transition:all .2s;}
.skey-in:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(99,102,241,.12);}
.skey-in::placeholder{color:var(--muted2);}
.seye{position:absolute;right:10px;background:none;border:none;color:var(--muted);cursor:pointer;font-size:14px;padding:3px;line-height:1;transition:color .2s;}
.seye:hover{color:var(--text);}
.scurr{font-size:10px;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-bottom:3px;}
.scurr span{color:var(--accent2);}
.sdivider{height:1px;background:var(--border-hi);margin:14px 0;}
.sdanger-title{font-size:10px;font-weight:700;color:var(--danger);margin-bottom:6px;letter-spacing:.07em;text-transform:uppercase;}
.sdanger-btn{width:100%;padding:9px;border-radius:7px;background:none;border:1px solid var(--danger);color:var(--danger);font-family:'Syne',sans-serif;font-size:11px;font-weight:700;cursor:pointer;transition:all .2s;letter-spacing:.04em;text-transform:uppercase;}
.sdanger-btn:hover{background:rgba(239,68,68,.08);}

/* memory panel */
#mem-panel{position:fixed;right:0;top:0;bottom:0;width:300px;background:var(--surface);border-left:1px solid var(--border-hi);z-index:200;transform:translateX(100%);transition:transform .3s cubic-bezier(.16,1,.3,1);display:flex;flex-direction:column;}
#mem-panel.open{transform:translateX(0);}
.mem-hdr{display:flex;align-items:center;justify-content:space-between;padding:13px 14px;border-bottom:1px solid var(--border);}
.mem-title{font-size:13px;font-weight:700;}
.mem-x{background:none;border:none;color:var(--muted);cursor:pointer;font-size:16px;padding:2px;}
.mem-x:hover{color:var(--text);}
.mem-list{flex:1;overflow-y:auto;padding:10px;}
.mem-item{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:9px 11px;margin-bottom:6px;position:relative;}
.mem-item-text{font-size:11px;line-height:1.6;}
.mem-item-meta{font-size:9px;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-top:4px;}
.mem-item-del{position:absolute;top:7px;right:8px;background:none;border:none;color:var(--muted);cursor:pointer;font-size:12px;opacity:0;transition:opacity .2s,color .2s;}
.mem-item:hover .mem-item-del{opacity:1;}
.mem-item-del:hover{color:var(--danger);}
.mem-empty{text-align:center;color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:11px;padding:28px 14px;}
.mem-add{padding:10px;border-top:1px solid var(--border);display:flex;gap:7px;}
.mem-add-in{flex:1;background:var(--surface2);border:1px solid var(--border);border-radius:6px;padding:7px 9px;color:var(--text);font-family:'JetBrains Mono',monospace;font-size:11px;outline:none;transition:border-color .2s;}
.mem-add-in:focus{border-color:var(--accent);}
.mem-add-btn{background:linear-gradient(135deg,var(--accent),var(--accent3));border:none;border-radius:6px;padding:7px 11px;color:#fff;font-family:'Syne',sans-serif;font-size:10px;font-weight:700;cursor:pointer;}

/* toast */
#toast{position:fixed;bottom:72px;left:50%;transform:translateX(-50%) translateY(14px);background:var(--surface2);border:1px solid var(--border-hi);border-radius:7px;padding:7px 13px;font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text);z-index:700;opacity:0;transition:all .3s;white-space:nowrap;pointer-events:none;box-shadow:0 8px 26px rgba(0,0,0,.4);}
#toast.show{opacity:1;transform:translateX(-50%) translateY(0);}

/* data analysis */
.da-card{margin-top:8px;background:var(--surface2);border:1px solid var(--border-hi);border-radius:12px;overflow:hidden;max-width:660px;}
.da-hdr{display:flex;align-items:center;gap:7px;padding:7px 11px;border-bottom:1px solid var(--border);font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--accent2);}
.da-stats{display:grid;grid-template-columns:repeat(5,1fr);background:var(--border);gap:1px;}
.da-stat{background:var(--surface2);padding:9px 10px;text-align:center;}
.da-val{font-size:16px;font-weight:800;color:var(--accent-h);font-family:'JetBrains Mono',monospace;}
.da-lbl{font-size:8px;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-top:2px;text-transform:uppercase;letter-spacing:.07em;}
.da-chart{padding:6px;}

/* responsive */
@media(max-width:700px){
  .tone-grid,.prov-grid{grid-template-columns:1fr;}
  .starters{grid-template-columns:1fr;}
  #art-panel.open{width:100%;position:absolute;inset:0;z-index:100;}
  .h-badge,.smodel{display:none;}
  .cap-chips{display:none;}
}
</style>

<!-- Hidden inputs -->
<input type="file" id="file-input" accept=".pdf,.txt,.md,.csv,.json,.js,.py,.html,.css,.tsv" multiple style="display:none">
<input type="file" id="img-input" accept="image/*" multiple style="display:none">
<input type="file" id="data-input" accept=".csv,.tsv,.json" multiple style="display:none">
<!-- Sandboxed JS runner -->
<iframe id="js-runner" sandbox="allow-scripts" style="display:none;width:0;height:0;"
  srcdoc="<script>window.addEventListener('message',e=>{let o='';try{const logs=[];const _c=console.log;console.log=(...a)=>{logs.push(a.map(x=>typeof x==='object'?JSON.stringify(x,null,2):String(x)).join(' '));};let r=eval(e.data);console.log=_c;const lo=logs.join('\n');if(r!==undefined)o=lo?(lo+'\n→ '+String(r)):('→ '+String(r));else o=lo||'(no output)';}catch(err){o='ERROR: '+err.message;}parent.postMessage({result:o,id:e.data.slice(0,8)},'*');});<\/script>">
</iframe>

<!-- ══ ONBOARDING ══ -->
<div id="onboarding">
  <div class="ob-inner">
    <div class="ob-logo">
      <div class="ob-icon">B</div>
      <div>
        <div class="ob-title-text">BAME <span>AI</span></div>
        <div class="ob-sub">// your personal research intelligence</div>
      </div>
    </div>

    <div class="ob-label">01 — Choose your vibe</div>
    <div class="tone-grid" id="ob-tone-grid">
      <div class="tone-card selected" data-tone="witty"><span class="tone-emoji">🎭</span><div class="tone-name">Witty & Playful</div><div class="tone-desc">Sharp humor, creative flair, accurate</div></div>
      <div class="tone-card" data-tone="professional"><span class="tone-emoji">🎯</span><div class="tone-name">Sharp & Professional</div><div class="tone-desc">Precise, authoritative, zero fluff</div></div>
      <div class="tone-card" data-tone="casual"><span class="tone-emoji">😎</span><div class="tone-name">Casual & Friendly</div><div class="tone-desc">Like texting your most brilliant friend</div></div>
      <div class="tone-card" data-tone="researcher"><span class="tone-emoji">🔬</span><div class="tone-name">Deep Researcher</div><div class="tone-desc">Thorough citations, academic precision</div></div>
    </div>

    <button class="ob-btn" id="ob-launch">Launch BAME AI →</button>
  </div>
</div>

<!-- ══ APP ══ -->
<div id="app">
  <header>
    <div class="h-left">
      <div class="h-icon">B</div>
      <div class="h-title">BAME <span>AI</span></div>
      <div class="h-badge" id="tone-badge">witty</div>
    </div>
    <div class="h-right">
      <button class="tone-pill" id="btn-vibe"><span id="tone-emoji">🎭</span> Vibe</button>
      <button class="hbtn" id="btn-research">🔬 Research</button>
      <button class="hbtn" id="btn-imggen">🎨 Image Gen</button>
      <button class="hbtn" id="btn-code">🧑‍💻 Code</button>
      <button class="hbtn" id="btn-memory">🧠 Memory</button>
      <button class="hbtn" id="btn-settings">⚙ Settings</button>
      <button class="hbtn" id="btn-export">Export</button>
      <button class="hbtn danger" id="btn-clear">Clear</button>
    </div>
  </header>

  <!-- CONVERSATION TABS -->
  <div id="conv-bar">
    <div class="ctab active" data-cid="0">
      <span class="ctab-name">New Chat</span>
      <button class="ctab-x" onclick="closeTab(event,0)">✕</button>
    </div>
    <button class="ctab-new" id="btn-new-tab" title="New conversation (Ctrl+T)">+</button>
  </div>

  <div class="status-bar">
    <div class="sdot" id="sdot"></div>
    <span class="stext" id="stext">Online — ready to go</span>
    <span class="smodel" id="smodel">Google · Gemini 2.5 Flash Lite</span>
  </div>

  <div id="layout">
    <div id="chat-side">
      <div id="chat"></div>
      <div id="scroll-btn" onclick="scrollBot()">↓</div>
      <div class="input-area">
        <div class="input-wrap">
          <div id="attach-strip"></div>
          <div class="input-row">
            <textarea id="userInput" rows="1" placeholder="Ask anything, drop a file, paste a URL, or describe an image to generate..." maxlength="32000"></textarea>
            <div class="input-tools">
              <button class="tbtn" id="tbtn-file" title="Attach PDF / document">📎</button>
              <button class="tbtn" id="tbtn-img" title="Attach image for analysis">🖼</button>
              <button class="tbtn" id="tbtn-data" title="Upload CSV/JSON for analysis">📊</button>
              <button class="tbtn on" id="tbtn-web" title="Toggle web search / scraping">🔍</button>
              <button class="tbtn" id="tbtn-voice" title="Voice input">🎤</button>
              <button class="send-btn" id="send-btn" disabled>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
              </button>
            </div>
          </div>
          <div class="input-footer">
            <span class="input-hint">↵ send · Shift+↵ newline · Ctrl+K focus · Ctrl+T new tab</span>
            <span class="char-count" id="char-count">0 / 32,000</span>
          </div>
        </div>
      </div>
    </div>

    <!-- ARTIFACT PANEL -->
    <div id="art-panel">
      <div class="art-hdr">
        <span class="art-title" id="art-title">Artifact</span>
        <span class="art-lang" id="art-lang">html</span>
        <div class="art-tabs">
          <button class="atab active" id="atab-pre" onclick="artTab('preview')">Preview</button>
          <button class="atab" id="atab-cod" onclick="artTab('code')">Code</button>
        </div>
        <div class="art-btns">
          <button class="abtn" onclick="artCopy()">📋</button>
          <button class="abtn" onclick="artDownload()">⬇</button>
          <button class="abtn" onclick="artFullscreen()">⛶</button>
        </div>
        <button class="art-close" onclick="artClose()">✕</button>
      </div>
      <div id="art-body">
        <div class="art-empty" id="art-empty"><span class="art-empty-icon">✦</span><span>Artifacts appear here</span></div>
        <iframe id="art-iframe" sandbox="allow-scripts allow-same-origin allow-forms" style="display:none"></iframe>
        <div id="art-code"><pre><code id="art-code-el"></code></pre></div>
      </div>
    </div>
  </div>
</div>

<!-- ══ VIBE MODAL ══ -->
<div id="modal-vibe" class="overlay">
  <div class="mbox">
    <div class="mtitle">Switch Your Vibe 🎨</div>
    <div class="tone-grid" id="modal-tone-grid">
      <div class="tone-card" data-tone="witty"><span class="tone-emoji">🎭</span><div class="tone-name">Witty & Playful</div><div class="tone-desc">Sharp humor, creative flair</div></div>
      <div class="tone-card" data-tone="professional"><span class="tone-emoji">🎯</span><div class="tone-name">Sharp & Professional</div><div class="tone-desc">Precise, zero fluff</div></div>
      <div class="tone-card" data-tone="casual"><span class="tone-emoji">😎</span><div class="tone-name">Casual & Friendly</div><div class="tone-desc">Genius friend energy</div></div>
      <div class="tone-card" data-tone="researcher"><span class="tone-emoji">🔬</span><div class="tone-name">Deep Researcher</div><div class="tone-desc">Thorough, cited, academic</div></div>
    </div>
    <div class="mactions">
      <button class="mbtn cancel" id="vibe-cancel">Cancel</button>
      <button class="mbtn ok" id="vibe-ok">Apply →</button>
    </div>
  </div>
</div>

<!-- ══ RESEARCH MODAL ══ -->
<div id="modal-research" class="overlay">
  <div class="mbox">
    <div class="mtitle">🔬 Deep Research Agent</div>
    <p style="font-size:11px;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-bottom:12px;line-height:1.65;">Auto-generates search queries, scrapes multiple web pages, and synthesises a comprehensive report with citations.</p>
    <input type="text" class="minput" id="research-q" placeholder="What do you want to research?">
    <span class="mlabel">Research depth</span>
    <div class="picker-row">
      <div class="picker-btn sel" data-depth="quick">⚡ Quick<br><span style="font-size:8px;color:var(--muted)">3 sources</span></div>
      <div class="picker-btn" data-depth="standard">📚 Standard<br><span style="font-size:8px;color:var(--muted)">6 sources</span></div>
      <div class="picker-btn" data-depth="deep">🔭 Deep<br><span style="font-size:8px;color:var(--muted)">12+ sources</span></div>
    </div>
    <div class="mactions">
      <button class="mbtn cancel" id="research-cancel">Cancel</button>
      <button class="mbtn ok" id="research-go">Start Research →</button>
    </div>
  </div>
</div>

<!-- ══ IMAGE GEN MODAL ══ -->
<div id="modal-imggen" class="overlay">
  <div class="mbox">
    <div class="mtitle">🎨 Image Generation</div>
    <p style="font-size:11px;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-bottom:12px;line-height:1.65;">Powered by Pollinations.ai — free, no key required.</p>
    <span class="mlabel">Image description</span>
    <textarea class="mcode" id="img-prompt" style="min-height:80px;resize:none;" placeholder="Describe the image you want to generate..."></textarea>
    <span class="mlabel" style="margin-top:10px;">Style preset</span>
    <div class="chips-wrap" id="style-chips">
      <div class="chip sel" data-style="">None</div>
      <div class="chip" data-style="photorealistic, ultra detailed, 8K">📷 Photorealistic</div>
      <div class="chip" data-style="digital art, vibrant, trending on artstation">🖌 Digital Art</div>
      <div class="chip" data-style="cinematic, film still, dramatic lighting">🎬 Cinematic</div>
      <div class="chip" data-style="watercolor illustration, soft pastel colors">🎨 Watercolor</div>
      <div class="chip" data-style="3D render, octane, studio lighting">🧊 3D Render</div>
      <div class="chip" data-style="anime style, studio ghibli inspired">🌸 Anime</div>
      <div class="chip" data-style="minimalist flat design, clean lines">✦ Minimal</div>
    </div>
    <span class="mlabel" style="margin-top:8px;">Size</span>
    <div class="picker-row">
      <div class="picker-btn sel" data-size="1024x1024">■ Square<br><span style="font-size:8px;color:var(--muted)">1024×1024</span></div>
      <div class="picker-btn" data-size="1792x1024">⬛ Wide<br><span style="font-size:8px;color:var(--muted)">1792×1024</span></div>
      <div class="picker-btn" data-size="1024x1792">▬ Portrait<br><span style="font-size:8px;color:var(--muted)">1024×1792</span></div>
    </div>
    <div class="mactions">
      <button class="mbtn cancel" id="imggen-cancel">Cancel</button>
      <button class="mbtn ok" id="imggen-go">Generate Image →</button>
    </div>
  </div>
</div>

<!-- ══ CODE INTERPRETER MODAL ══ -->
<div id="modal-code" class="overlay">
  <div class="mbox" style="max-width:660px;">
    <div class="mtitle">🧑‍💻 Code Interpreter</div>
    <p style="font-size:11px;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-bottom:12px;line-height:1.65;">Run JavaScript in a sandboxed iframe. Captures <code style="background:var(--surface2);padding:1px 4px;border-radius:3px;font-size:10px;">console.log</code> output and return values.</p>
    <div style="display:flex;gap:7px;margin-bottom:8px;align-items:center;">
      <span class="mlabel" style="margin:0;">Code</span>
      <button class="tbtn" id="ci-ai-btn" title="Ask AI to write code">✨ AI Write</button>
      <button class="tbtn" id="ci-clear-btn">Clear</button>
    </div>
    <textarea class="mcode" id="ci-editor" placeholder="// Write JavaScript here&#10;const nums = [1,2,3,4,5];&#10;const sum = nums.reduce((a,b)=>a+b,0);&#10;console.log('Sum:', sum);&#10;sum"></textarea>
    <div class="mout" id="ci-output" style="display:none"></div>
    <div style="display:flex;align-items:center;gap:8px;margin-top:9px;">
      <button class="mbtn go" id="ci-run" style="flex:0;padding:8px 16px;">▶ Run</button>
      <span style="font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted);" id="ci-status"></span>
      <button class="mbtn cancel" id="ci-close" style="flex:0;padding:8px 12px;margin-left:auto;">Close</button>
    </div>
  </div>
</div>

<!-- ══ SETTINGS MODAL ══ -->
<div id="modal-settings" class="overlay">
  <div class="mbox" style="max-width:440px;">
    <div class="mtitle">⚙️ Settings</div>
    <div style="padding:10px 0 14px;color:var(--muted);font-family:'JetBrains Mono',monospace;font-size:11px;">Model: Google · Gemini 2.5 Flash Lite</div>
    <div class="mactions">
      <button class="mbtn cancel" id="s-cancel">Cancel</button>
    </div>
  </div>
</div>

<!-- ══ MEMORY PANEL ══ -->
<div id="mem-panel">
  <div class="mem-hdr">
    <div class="mem-title">🧠 Memory</div>
    <button class="mem-x" id="mem-close">✕</button>
  </div>
  <div class="mem-list" id="mem-list"></div>
  <div class="mem-add">
    <input type="text" class="mem-add-in" id="mem-in" placeholder="Add a memory...">
    <button class="mem-add-btn" id="mem-add-btn">Add</button>
  </div>
</div>

<div id="toast"></div>
<script>
// ══════════════════════════════════════════════════════════════════════
// PROVIDERS
// ══════════════════════════════════════════════════════════════════════
const PROVIDERS = {
  google:    { name:'Google Gemini', model:'Gemini 2.5 Flash Lite',    placeholder:'AIza...',     hint:'Free key: <a href="https://aistudio.google.com/apikey" target="_blank">aistudio.google.com</a>' },
  openai:    { name:'OpenAI',        model:'GPT-4o',               placeholder:'sk-...',      hint:'Key: <a href="https://platform.openai.com/api-keys" target="_blank">platform.openai.com</a>' },
  anthropic: { name:'Anthropic',     model:'Claude Sonnet',        placeholder:'sk-ant-...', hint:'Key: <a href="https://console.anthropic.com" target="_blank">console.anthropic.com</a>' },
};

// ══════════════════════════════════════════════════════════════════════
// SYSTEM PROMPTS
// ══════════════════════════════════════════════════════════════════════
const ART_SYS = `
ARTIFACT SYSTEM — You can render live visual artifacts. Use these tags:
<artifact type="html" title="App"><!DOCTYPE html>...</artifact>
<artifact type="svg" title="Diagram"><svg>...</svg></artifact>
<artifact type="javascript" title="Script">// code</artifact>
<artifact type="python" title="Script"># code</artifact>
<artifact type="markdown" title="Doc"># content</artifact>
<artifact type="csv" title="Data">col1,col2\nval1,val2</artifact>

RULES: HTML artifacts = fully self-contained, all CSS/JS inline. CDN allowed: cdnjs.cloudflare.com only. ONE artifact per message. Make artifacts spectacular — full color, animation, interactivity. For data analysis, create beautiful Chart.js dashboards in HTML artifacts. Never reveal your underlying model.`;

const TONES = {
  witty:      { emoji:'🎭', label:'Witty & Playful',    sys:'You are BAME AI — brilliantly intelligent with razor-sharp wit and playful charm. Deliver accurate answers with humor. Build stunning interactive artifacts. Use markdown beautifully.' },
  professional:{ emoji:'🎯', label:'Sharp & Professional',sys:'You are BAME AI — an elite intelligence. Direct, authoritative, exhaustively thorough. Expert analysis, clean structured markdown, production-quality artifacts.' },
  casual:     { emoji:'😎', label:'Casual & Friendly',   sys:'You are BAME AI — like texting your most brilliant friend. Warm, approachable, never condescending. Helpful, accurate, fun artifacts.' },
  researcher: { emoji:'🔬', label:'Deep Researcher',     sys:'You are BAME AI — a meticulous research AI. Deeply sourced, nuanced analysis. Always cite inline with [Source N]. Structure responses with clear sections. Create data visualisation artifacts.' },
};

// ══════════════════════════════════════════════════════════════════════
// STATE
// ══════════════════════════════════════════════════════════════════════
const API_SERVER = 'http://localhost:5000';
let S = { tone:'witty', thinking:false, webSearch:true };
let conversations = [];   // [{id, name, messages:[]}]
let activeConvId = 0;
let memories = [];
let attachments = [];
let currentArt = null;

function getConv(id){ return conversations.find(c=>c.id===id); }
function activeConv(){ return getConv(activeConvId); }
function msgs(){ return activeConv()?.messages || []; }

function load(){
  try{
    const d = JSON.parse(localStorage.getItem('bame_v4')||'{}');
    S.tone = d.tone||'witty';
    memories = d.memories||[];
    conversations = d.convs||[];
  }catch(e){}
  if(!conversations.length){ conversations=[{id:0,name:'New Chat',messages:[]}]; activeConvId=0; }
  else activeConvId = conversations[0].id;
}
function save(){
  try{ localStorage.setItem('bame_v4', JSON.stringify({
    tone:S.tone, memories,
    convs: conversations.map(c=>({...c, messages:c.messages.slice(-80)}))
  })); }catch(e){}
}
load();

// ══════════════════════════════════════════════════════════════════════
// API CALLS — proxied through Flask server at API_SERVER
// ══════════════════════════════════════════════════════════════════════
function buildSys(){
  const base = TONES[S.tone].sys + ART_SYS;
  const memCtx = memories.length ? `\n\nUSER MEMORY:\n${memories.map(m=>'- '+m.text).join('\n')}` : '';
  return base + memCtx;
}

async function callAPI(messages, onChunk){
  const sys = buildSys();
  const m = messages || msgs().slice(-50);
  if(onChunk){
    const r = await fetch(`${API_SERVER}/api/stream`, {
      method:'POST', headers:{'Content-Type':'application/json'},
      body:JSON.stringify({messages:m, system:sys})
    });
    if(!r.ok){ const e=await r.json().catch(()=>({})); throw new Error(e?.error||`HTTP ${r.status}`); }
    const reader=r.body.getReader(); const dec=new TextDecoder(); let full=''; let buf='';
    while(true){
      const{done,value}=await reader.read(); if(done)break;
      buf+=dec.decode(value);
      const parts=buf.split('\n\n'); buf=parts.pop()||'';
      for(const part of parts){
        if(!part.startsWith('data:'))continue;
        const d=part.slice(5).trim(); if(d==='[DONE]')continue;
        try{ const p=JSON.parse(d); if(p.error) throw new Error(p.error); const t=p.text||''; if(t){full+=t;onChunk(t);} }catch(e){ if(e.message&&!e.message.startsWith('JSON')) throw e; }
      }
    }
    return full;
  }
  const r = await fetch(`${API_SERVER}/api/chat`, {
    method:'POST', headers:{'Content-Type':'application/json'},
    body:JSON.stringify({messages:m, system:sys})
  });
  if(!r.ok){ const e=await r.json().catch(()=>({})); throw new Error(e?.error||`HTTP ${r.status}`); }
  const d = await r.json();
  if(d.error) throw new Error(d.error);
  return d.content;
}

async function callSimple(prompt){
  const r = await fetch(`${API_SERVER}/api/chat`, {
    method:'POST', headers:{'Content-Type':'application/json'},
    body:JSON.stringify({messages:[{role:'user',content:prompt}], system:'You are a helpful assistant. Be concise and precise.'})
  });
  if(!r.ok){ const e=await r.json().catch(()=>({})); throw new Error(e?.error||`HTTP ${r.status}`); }
  const d = await r.json();
  if(d.error) throw new Error(d.error);
  return d.content;
}

// ══════════════════════════════════════════════════════════════════════
// WEB SCRAPING
// ══════════════════════════════════════════════════════════════════════
const URL_RE = /https?:\/\/[^\s<>"{}|\\^`\[\]]+/gi;

async function scrapeURL(url){
  try{
    const r = await fetch(`${API_SERVER}/api/scrape`,
      { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({url}),
        signal:AbortSignal.timeout(10000) });
    if(!r.ok) throw new Error('fetch failed');
    const d = await r.json();
    const html = d.contents||'';
    const tmp = document.createElement('div');
    tmp.innerHTML = html.replace(/<script[\s\S]*?<\/script>/gi,'').replace(/<style[\s\S]*?<\/style>/gi,'');
    const text = tmp.innerText.replace(/\s+/g,' ').trim().slice(0,6000);
    const title = (html.match(/<title[^>]*>(.*?)<\/title>/i)||['',''])[1].replace(/&amp;/g,'&').trim() || url;
    return { url, title, text };
  }catch(e){ return { url, title:url, text:`(Could not scrape: ${e.message})` }; }
}

// ══════════════════════════════════════════════════════════════════════
// RESEARCH AGENT
// ══════════════════════════════════════════════════════════════════════
const DEPTH = { quick:{q:2,p:2}, standard:{q:3,p:3}, deep:{q:5,p:4} };
let researchDepth = 'quick';

async function runResearch(query, depth){
  const cfg = DEPTH[depth]||DEPTH.quick;
  S.thinking = true;
  document.getElementById('welcome')?.remove();
  const conv = activeConv(); if(conv) conv.messages.push({role:'user',content:`[Research]: ${query}`});
  renderMsg('user', `🔬 Researching: **${query}**`);

  const thEl = renderThinking();
  try{
    // Step 1: Generate queries
    setThink(thEl, '🧠 Generating search queries...');
    let queries;
    try{
      const qr = await callSimple(`Generate ${cfg.q} distinct search queries to research: "${query}". Return ONLY a JSON array of strings.`);
      queries = JSON.parse(qr.replace(/```json|```/g,'').trim());
      if(!Array.isArray(queries)) throw new Error('not array');
    }catch(e){
      queries = [query, `${query} overview`, `${query} 2025`, `${query} explained`, `${query} latest`].slice(0,cfg.q);
    }

    // Step 2: Scrape sources
    const pages = [];
    for(let i=0;i<queries.length;i++){
      const q = queries[i];
      setThink(thEl, `🔍 Searching: "${q}" (${i+1}/${queries.length})`);
      try{
        const sr = await fetch(`${API_SERVER}/api/search`,
          {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({query:q}),signal:AbortSignal.timeout(9000)});
        const sd = await sr.json();
        const urls = [...sd.contents.matchAll(/href="(https?:\/\/[^"]+)"/g)]
          .map(m=>m[1]).filter(u=>!u.includes('duckduckgo')&&!u.includes('google')&&u.startsWith('http'))
          .slice(0,cfg.p);
        for(const url of urls){
          setThink(thEl, `📄 Scraping: ${url.slice(0,55)}...`);
          const p = await scrapeURL(url);
          if(p.text&&p.text.length>150) pages.push(p);
        }
      }catch(e){}
    }

    // Step 3: Synthesise
    setThink(thEl, `✍️ Synthesising ${pages.length} sources...`);
    const ctx = pages.slice(0,12).map((p,i)=>`[Source ${i+1}] ${p.title}\nURL: ${p.url}\n${p.text}`).join('\n\n---\n\n');
    const synPrompt = `You are a world-class research analyst. Write a comprehensive report on: "${query}"\n\nSOURCE MATERIAL:\n${ctx}\n\nWrite with: Executive Summary, Key Findings (cite [Source N]), Detailed Analysis, Conclusions. If sources are sparse, supplement with your knowledge but note it clearly. Be genuinely comprehensive and impressive.`;
    
    thEl.remove();
    const streamDiv = createStreamDiv();
    const bub = streamDiv.querySelector('.msg-bubble');
    let reply = '';
    try{
      reply = await callAPI([{role:'user',content:synPrompt}], chunk=>{ reply+=chunk; bub.innerHTML=renderMD(reply)+'<span class="stream-cur"></span>'; scrollBot(); });
    }catch(e){ reply = await callSimple(synPrompt); bub.innerHTML = renderMD(reply); }
    finaliseStream(streamDiv, reply, pages);

    if(conv){ conv.messages.push({role:'assistant',content:reply.replace(/<artifact[\s\S]*?<\/artifact>/gi,'[artifact]')}); }
    save();
    setStatus('ready', `✅ Research complete — ${pages.length} sources`);
  }catch(err){
    thEl.remove();
    renderMsg('ai', `**Research failed:** ${err.message}`, true);
    setStatus('ready', 'Error');
  }
  S.thinking = false;
}

// ══════════════════════════════════════════════════════════════════════
// IMAGE GENERATION
// ══════════════════════════════════════════════════════════════════════
let imgStyle = '', imgSize = '1024x1024';

async function generateImage(prompt){
  document.getElementById('welcome')?.remove();
  const conv = activeConv();
  if(conv) conv.messages.push({role:'user',content:`Generate image: ${prompt}`});
  renderMsg('user', `🎨 Generate image: ${prompt}`);
  S.thinking = true;
  setStatus('thinking', '🎨 Generating image...');
  const thEl = renderThinking();
  setThink(thEl, '🎨 Calling image generation API...');
  try{
    let imgUrl = '', revisedPrompt = prompt;
    const fullPrompt = imgStyle ? `${prompt}, ${imgStyle}` : prompt;

    const imgR = await fetch(`${API_SERVER}/api/image`, {
      method:'POST', headers:{'Content-Type':'application/json'},
      body:JSON.stringify({prompt:fullPrompt, size:imgSize})
    });
    if(!imgR.ok){ const e=await imgR.json().catch(()=>({})); throw new Error(e?.error||`HTTP ${imgR.status}`); }
    const imgD = await imgR.json();
    if(imgD.error) throw new Error(imgD.error);
    imgUrl = imgD.url;
    revisedPrompt = imgD.revised_prompt || prompt;

    thEl.remove();
    const chat = document.getElementById('chat');
    const div = document.createElement('div');
    div.className = 'msg ai';
    div.innerHTML = `
      <div class="msg-av">B</div>
      <div class="msg-body">
        <div class="msg-meta"><span style="font-weight:700">BAME AI</span><span style="color:var(--muted2);margin-left:5px;">${now()}</span></div>
        <div class="img-result">
          <div class="img-result-hdr">🎨 Generated · ${imgSize} · Pollinations.ai</div>
          <img src="${imgUrl}" class="gen-img" alt="${esc(prompt)}">
          <div class="img-result-btns">
            <a class="img-abtn" href="${imgUrl}" target="_blank">🔗 Open</a>
            ${imgUrl.startsWith('data:') ? '' : `<a class="img-abtn" href="${imgUrl}" download="bame-image.png">⬇ Download</a>`}
            <button class="img-abtn" onclick="copyText('${imgUrl.startsWith('data:') ? 'data:URI (too long to copy)' : imgUrl}')">📋 URL</button>
          </div>
        </div>
        <div class="msg-bubble" style="margin-top:5px;font-size:11px;color:var(--muted);">Prompt: ${esc(revisedPrompt.slice(0,180))}${revisedPrompt.length>180?'…':''}</div>
        <div class="msg-actions">
          <button class="act-btn" onclick="document.getElementById('img-prompt').value='${esc(prompt).replace(/'/g,"\\'")}';openModal('modal-imggen')">↺ Regenerate</button>
        </div>
      </div>`;
    chat.appendChild(div);
    if(conv) conv.messages.push({role:'assistant',content:`[Generated image from: ${prompt}]`});
    save();
    setStatus('ready', '✅ Image generated');
    scrollBot();
  }catch(err){
    thEl.remove();
    renderMsg('ai', `**Image generation failed:** ${err.message}`, true);
    setStatus('ready', 'Error');
    showToast('❌ '+err.message);
  }
  S.thinking = false;
}

// ══════════════════════════════════════════════════════════════════════
// CODE INTERPRETER
// ══════════════════════════════════════════════════════════════════════
let ciResolve = null;
window.addEventListener('message', e => {
  if(e.data && typeof e.data === 'object' && 'result' in e.data && ciResolve){ ciResolve(e.data.result); ciResolve=null; }
});

async function runCode(code){
  return new Promise((res,rej)=>{
    ciResolve = res;
    setTimeout(()=>{ if(ciResolve){ ciResolve=null; rej(new Error('Timeout after 5s')); } }, 5000);
    document.getElementById('js-runner').contentWindow.postMessage(code,'*');
  });
}

document.getElementById('ci-run').addEventListener('click', async()=>{
  const code = document.getElementById('ci-editor').value.trim();
  if(!code) return;
  const btn=document.getElementById('ci-run'); btn.disabled=true; btn.textContent='⏳';
  const out=document.getElementById('ci-output'); const st=document.getElementById('ci-status');
  try{
    // Wrap code to capture console.log
    const wrapped = `(function(){let logs=[];const _l=console.log;console.log=(...a)=>{logs.push(a.map(x=>typeof x==='object'?JSON.stringify(x,null,2):String(x)).join(' '));};let r;try{r=eval(${JSON.stringify(code)});}catch(e){console.log=_l;return'ERROR: '+e.message;}console.log=_l;const lo=logs.join('\\n');return r!==undefined?(lo?lo+'\\n→ '+String(r):'→ '+String(r)):(lo||'(no output)');})()`;
    const result = await runCode(wrapped);
    out.textContent = result; out.className = result.startsWith('ERROR:') ? 'mout err' : 'mout';
    st.textContent = result.startsWith('ERROR:') ? '❌ Error' : `✅ Done`;
  }catch(err){ out.textContent='ERROR: '+err.message; out.className='mout err'; st.textContent='❌ Timeout'; }
  out.style.display='block'; btn.disabled=false; btn.textContent='▶ Run';
});

document.getElementById('ci-clear-btn').addEventListener('click',()=>{
  document.getElementById('ci-editor').value='';
  document.getElementById('ci-output').style.display='none';
  document.getElementById('ci-status').textContent='';
});

document.getElementById('ci-ai-btn').addEventListener('click', async()=>{
  const ta = document.getElementById('ci-editor');
  const req = prompt('What should the code do?'); if(!req) return;
  document.getElementById('ci-status').textContent='✨ Writing...';
  try{
    const code = await callSimple(`Write JavaScript that: ${req}\nReturn ONLY the code, no markdown, no explanation. Use console.log() to output results.`);
    ta.value = code.replace(/```javascript|```js|```/g,'').trim();
    document.getElementById('ci-run').click();
  }catch(e){ showToast('❌ '+e.message); }
  document.getElementById('ci-status').textContent='';
});

document.getElementById('ci-close').addEventListener('click',()=>closeModal('modal-code'));

// ══════════════════════════════════════════════════════════════════════
// FILE PROCESSING
// ══════════════════════════════════════════════════════════════════════
pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

async function processPDF(file){
  return new Promise((res,rej)=>{
    const fr=new FileReader();
    fr.onload=async e=>{
      try{
        const pdf=await pdfjsLib.getDocument({data:e.target.result}).promise;
        let text='';
        for(let i=1;i<=Math.min(pdf.numPages,25);i++){
          const pg=await pdf.getPage(i);
          const c=await pg.getTextContent();
          text+=c.items.map(s=>s.str).join(' ')+'\n';
        }
        res(text.trim().slice(0,10000));
      }catch(err){rej(err);}
    };
    fr.readAsArrayBuffer(file);
  });
}

async function processText(file){ return new Promise((r,j)=>{ const fr=new FileReader(); fr.onload=e=>r(e.target.result.slice(0,10000)); fr.onerror=j; fr.readAsText(file); }); }
async function processImage(file){ return new Promise((r,j)=>{ const fr=new FileReader(); fr.onload=e=>r(e.target.result); fr.onerror=j; fr.readAsDataURL(file); }); }
function fmtBytes(b){ return b>1e6?(b/1e6).toFixed(1)+'MB':b>1e3?Math.round(b/1e3)+'KB':b+'B'; }

async function handleFiles(files, type='file'){
  for(const file of files){
    setStatus('thinking', `Reading ${file.name}...`);
    try{
      if(type==='image'||file.type.startsWith('image/')){
        const data = await processImage(file);
        attachments.push({type:'image',name:file.name,content:data,mimeType:file.type,size:fmtBytes(file.size)});
      } else if(file.name.endsWith('.pdf')){
        const text = await processPDF(file);
        attachments.push({type:'file',name:file.name,content:text,mimeType:'application/pdf',size:fmtBytes(file.size)});
      } else {
        const text = await processText(file);
        attachments.push({type:'file',name:file.name,content:text,mimeType:file.type,size:fmtBytes(file.size)});
      }
      showToast(`📎 ${file.name} attached`);
      renderAttachStrip();
    }catch(err){ showToast(`❌ Failed: ${file.name}`); }
  }
  setStatus('ready','Online — ready to go');
  document.getElementById('send-btn').disabled=false;
}

document.getElementById('tbtn-file').addEventListener('click',()=>document.getElementById('file-input').click());
document.getElementById('tbtn-img').addEventListener('click',()=>document.getElementById('img-input').click());
document.getElementById('tbtn-data').addEventListener('click',()=>document.getElementById('data-input').click());
document.getElementById('file-input').addEventListener('change',e=>{ handleFiles(e.target.files,'file'); e.target.value=''; });
document.getElementById('img-input').addEventListener('change',e=>{ handleFiles(e.target.files,'image'); e.target.value=''; });
document.getElementById('data-input').addEventListener('change',async e=>{
  for(const file of e.target.files){
    const text = await processText(file);
    attachments.push({type:'data',name:file.name,content:text,mimeType:file.type,size:fmtBytes(file.size)});
    // pre-fill input
    const ta=document.getElementById('userInput');
    if(!ta.value) ta.value=`Analyse the data in ${file.name} and create an interactive visualisation`;
    autoResize(); document.getElementById('send-btn').disabled=false;
    showToast(`📊 ${file.name} ready`);
    renderAttachStrip();
  }
  e.target.value='';
});

function renderAttachStrip(){
  const strip=document.getElementById('attach-strip');
  strip.innerHTML=attachments.map((a,i)=>`
    <div class="atch">
      <span class="atch-ic">${a.type==='image'?'🖼':a.type==='data'?'📊':'📄'}</span>
      <span class="atch-name">${esc(a.name)}</span>
      <span class="atch-sz">${a.size}</span>
      <button class="atch-rm" onclick="removeAttach(${i})">✕</button>
    </div>`).join('');
}
function removeAttach(i){ attachments.splice(i,1); renderAttachStrip(); }

// Drag & drop
document.addEventListener('dragover',e=>e.preventDefault());
document.addEventListener('drop',async e=>{
  e.preventDefault();
  await handleFiles(Array.from(e.dataTransfer.files));
});

// ══════════════════════════════════════════════════════════════════════
// VOICE INPUT
// ══════════════════════════════════════════════════════════════════════
let recog=null, isRec=false;
const voiceBtn=document.getElementById('tbtn-voice');
if('SpeechRecognition' in window||'webkitSpeechRecognition' in window){
  const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  recog=new SR(); recog.continuous=false; recog.interimResults=true; recog.lang='en-US';
  recog.onresult=e=>{ const t=Array.from(e.results).map(r=>r[0].transcript).join(''); document.getElementById('userInput').value=t; autoResize(); document.getElementById('send-btn').disabled=false; if(e.results[0].isFinal) stopRec(); };
  recog.onend=()=>stopRec(); recog.onerror=()=>stopRec();
  voiceBtn.addEventListener('click',()=>isRec?stopRec():startRec());
} else { voiceBtn.style.opacity='.3'; voiceBtn.style.cursor='not-allowed'; voiceBtn.title='Not supported in this browser'; }

function startRec(){ if(!recog)return; recog.start(); isRec=true; voiceBtn.classList.add('rec'); voiceBtn.title='Listening… click to stop'; setStatus('thinking','🎤 Listening...'); }
function stopRec(){ if(recog&&isRec){ try{recog.stop();}catch(e){} } isRec=false; voiceBtn.classList.remove('rec'); voiceBtn.title='Voice input'; setStatus('ready','Online — ready to go'); }

// ══════════════════════════════════════════════════════════════════════
// SEND MESSAGE
// ══════════════════════════════════════════════════════════════════════
const ta=document.getElementById('userInput');
const sendBtn=document.getElementById('send-btn');

ta.addEventListener('input',()=>{ autoResize(); const l=ta.value.length; const cc=document.getElementById('char-count'); cc.textContent=`${l.toLocaleString()} / 32,000`; cc.className='char-count'+(l>28000?' crit':l>20000?' warn':''); sendBtn.disabled=l===0&&attachments.length===0||S.thinking; });
ta.addEventListener('keydown',e=>{ if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();if(!sendBtn.disabled)sendMessage();} });
sendBtn.addEventListener('click',sendMessage);
document.getElementById('tbtn-web').addEventListener('click',()=>{ S.webSearch=!S.webSearch; document.getElementById('tbtn-web').classList.toggle('on',S.webSearch); showToast(S.webSearch?'🔍 Web search ON':'🔍 Web search OFF'); });

function autoResize(){ ta.style.height='auto'; ta.style.height=Math.min(ta.scrollHeight,140)+'px'; }

async function sendMessage(){
  const text=ta.value.trim();
  if((!text&&attachments.length===0)||S.thinking) return;

  document.getElementById('welcome')?.remove();

  // Detect image generation intent
  if(text && isImgIntent(text)){
    const prompt=text.replace(/^(generate|create|draw|make|design|paint|render|imagine|show me)\s+(an?\s+)?(image|picture|photo|illustration|art|painting|drawing|portrait|landscape)(?:\s+of)?/i,'').trim()||text;
    ta.value=''; autoResize(); sendBtn.disabled=true;
    await generateImage(prompt);
    return;
  }

  const conv=activeConv();
  const localAttach=[...attachments]; attachments=[]; renderAttachStrip();

  // Build user message content
  let userText=text;
  const fileCtx=localAttach.filter(a=>a.type!=='image').map(a=>`\n\n[Attached ${a.type==='data'?'data file':'file'}: ${a.name}]\n${a.content}`).join('');
  const imgAttach=localAttach.filter(a=>a.type==='image');
  if(imgAttach.length) userText+='\n\n'+imgAttach.map(a=>`[Attached image: ${a.name} — please analyse this image based on my request]`).join('\n');
  const fullContent=userText+(fileCtx||'');

  if(conv) conv.messages.push({role:'user',content:fullContent});
  save();

  ta.value=''; autoResize(); document.getElementById('char-count').textContent='0 / 32,000'; sendBtn.disabled=true;
  renderMsg('user', userText, false, true, [], localAttach);

  S.thinking=true; setStatus('thinking','Thinking...');

  // Auto-name conversation
  if(conv&&conv.name==='New Chat'&&text) { conv.name=text.slice(0,30)+(text.length>30?'…':''); renderTabs(); save(); }

  // URL scraping
  if(S.webSearch){
    const urls=(text.match(URL_RE)||[]).filter(u=>!u.match(/\.(png|jpg|gif|svg|ico|webp)$/i));
    if(urls.length>0){
      const thEl=renderThinking();
      for(const url of urls.slice(0,3)){
        setThink(thEl,`🌐 Scraping ${url.slice(0,55)}...`);
        const pg=await scrapeURL(url);
        if(conv) conv.messages[conv.messages.length-1].content += `\n\n[Web content: ${pg.title}]\n${pg.text}`;
      }
      thEl.remove();
    }
  }

  const thEl=renderThinking();
  try{
    const streamDiv=createStreamDiv();
    const bub=streamDiv.querySelector('.msg-bubble');
    thEl.remove();
    let reply='';
    reply=await callAPI(null, chunk=>{ reply+=chunk; bub.innerHTML=renderMD(reply)+'<span class="stream-cur"></span>'; scrollBot(); });
    finaliseStream(streamDiv, reply);
    if(conv){ conv.messages.push({role:'assistant',content:reply.replace(/<artifact[\s\S]*?<\/artifact>/gi,'[artifact]')}); save(); }
    setStatus('ready','Online — ready to go');
  }catch(err){
    try{thEl.remove();}catch(e){}
    renderMsg('ai',`**Error:** ${err.message}`,true);
    setStatus('ready','Error'); showToast('❌ '+(err.message||'API Error'));
  }
  S.thinking=false; sendBtn.disabled=ta.value.trim()===''&&attachments.length===0;
  scrollBot();
}

function isImgIntent(t){
  return /^(generate|create|draw|make|design|paint|render|imagine|show me)\s+(an?\s+)?(image|picture|photo|illustration|artwork|painting|portrait|landscape)\b/i.test(t);
}

// ══════════════════════════════════════════════════════════════════════
// STREAMING UI
// ══════════════════════════════════════════════════════════════════════
function createStreamDiv(){
  const chat=document.getElementById('chat');
  const d=document.createElement('div'); d.className='msg ai'; d.id='stream-msg';
  d.innerHTML=`<div class="msg-av">B</div><div class="msg-body"><div class="msg-meta"><span style="font-weight:700">BAME AI</span><span style="color:var(--muted2);margin-left:5px;">${now()}</span></div><div class="msg-bubble"></div></div>`;
  chat.appendChild(d); scrollBot(); return d;
}

function finaliseStream(div, fullReply, sources=[]){
  div.id='';
  const bub=div.querySelector('.msg-bubble');
  bub.innerHTML=renderMD(fullReply);

  // Syntax highlight
  div.querySelectorAll('pre code').forEach(block=>{
    if(!block.parentElement.querySelector('.code-hdr')){
      hljs.highlightElement(block);
      const pre=block.parentElement;
      const lang=(block.className.match(/language-(\w+)/)||[])[1]||'code';
      const hdr=document.createElement('div'); hdr.className='code-hdr';
      hdr.innerHTML=`<span class="code-lang">${lang}</span><button class="copy-btn" onclick="copyCode(this)">Copy</button>`;
      pre.insertBefore(hdr,block);
    }
  });

  // Sources
  if(sources.length>0){
    const sp=document.createElement('div'); sp.className='sources-row';
    sp.innerHTML=`<div class="src-label">📚 ${sources.length} sources</div><div class="src-chips">${sources.map((s,i)=>`<a class="src-chip" href="${s.url}" target="_blank">🔗 ${esc(s.title.slice(0,40)||`Source ${i+1}`)}</a>`).join('')}</div>`;
    div.querySelector('.msg-body').appendChild(sp);
  }

  // Actions
  const acts=document.createElement('div'); acts.className='msg-actions';
  acts.innerHTML=`<button class="act-btn" onclick="copyBubble(this)">📋 Copy</button><button class="act-btn" onclick="regen()">↺ Regen</button>`;
  div.querySelector('.msg-body').appendChild(acts);

  // Artifact
  const art=parseArt(fullReply);
  if(art) setTimeout(()=>openArt(art),200);
}

// ══════════════════════════════════════════════════════════════════════
// RENDER MESSAGES
// ══════════════════════════════════════════════════════════════════════
marked.setOptions({breaks:true,gfm:true});

function renderAllMsgs(){
  document.getElementById('chat').innerHTML='';
  (activeConv()?.messages||[]).forEach(m=>renderMsg(m.role==='user'?'user':'ai',m.content,false,false));
  scrollBot();
}

function renderMsg(type,content,isErr=false,animate=true,sources=[],localAttach=[]){
  const chat=document.getElementById('chat');
  const isAI=type==='ai';
  const art=isAI?parseArt(content):null;
  const displayContent=art?artStrip(content):content;
  const div=document.createElement('div');
  div.className=`msg ${type}`; if(!animate)div.style.animation='none';
  const bodyHTML=isAI?renderMD(displayContent):escChat(content);
  const imgHTML=localAttach.filter(a=>a.type==='image').map(a=>`<img src="${a.content}" class="msg-img" alt="${esc(a.name)}">`).join('');
  const fileHTML=localAttach.filter(a=>a.type!=='image').map(a=>`<div class="atch" style="margin-top:5px;display:inline-flex;"><span class="atch-ic">📄</span><span class="atch-name">${esc(a.name)}</span><span class="atch-sz">${a.size}</span></div>`).join('');
  const artHTML=art?`<div class="art-pill" onclick="openArt(${JSON.stringify(art).replace(/"/g,'&quot;')})"><span class="art-pill-ic">${artIcon(art.type)}</span><div class="art-pill-info"><div class="art-pill-title">${esc(art.title)}</div><div class="art-pill-meta">${art.type} · click to open</div></div><span class="art-pill-arr">→</span></div>`:'';
  const srcHTML=sources.length?`<div class="sources-row"><div class="src-label">📚 ${sources.length} sources</div><div class="src-chips">${sources.map((s,i)=>`<a class="src-chip" href="${s.url}" target="_blank">🔗 ${esc(s.title.slice(0,38)||`Source ${i+1}`)}</a>`).join('')}</div></div>`:'';
  div.innerHTML=`
    <div class="msg-av">${isAI?'B':'👤'}</div>
    <div class="msg-body">
      <div class="msg-meta"><span style="font-weight:700">${isAI?'BAME AI':'You'}</span><span style="color:var(--muted2);margin-left:5px;">${now()}</span></div>
      ${imgHTML}${fileHTML}
      ${bodyHTML?`<div class="msg-bubble">${bodyHTML}</div>`:''}
      ${artHTML}${srcHTML}
      ${isAI?`<div class="msg-actions"><button class="act-btn" onclick="copyBubble(this)">📋 Copy</button><button class="act-btn" onclick="regen()">↺ Regen</button></div>`:''}
    </div>`;
  chat.appendChild(div);
  div.querySelectorAll('pre code').forEach(block=>{
    hljs.highlightElement(block);
    const pre=block.parentElement;
    if(pre.querySelector('.code-hdr'))return;
    const lang=(block.className.match(/language-(\w+)/)||[])[1]||'code';
    const hdr=document.createElement('div'); hdr.className='code-hdr';
    hdr.innerHTML=`<span class="code-lang">${lang}</span><button class="copy-btn" onclick="copyCode(this)">Copy</button>`;
    pre.insertBefore(hdr,block);
  });
  if(art&&animate)setTimeout(()=>openArt(art),200);
  scrollBot(); return div;
}

function renderThinking(){
  const chat=document.getElementById('chat');
  const d=document.createElement('div'); d.className='msg ai thinking-msg';
  d.innerHTML=`<div class="msg-av">B</div><div class="msg-body"><div class="msg-meta"><span style="font-weight:700">BAME AI</span></div><div class="msg-bubble"><div class="thinking-bubble"><div class="dots"><span></span><span></span><span></span></div><span id="think-txt">Thinking...</span></div></div></div>`;
  document.getElementById('chat').appendChild(d); scrollBot(); return d;
}
function setThink(el,t){ const s=el.querySelector('#think-txt'); if(s)s.textContent=t; scrollBot(); }

function renderMD(t){
  // Protect LaTeX blocks from marked processing
  const latexBlocks = [];
  t = t.replace(/\$\$[\s\S]+?\$\$|\\\[[\s\S]+?\\\]/g, m => { latexBlocks.push({type:'block',src:m}); return `LATEXBLOCK${latexBlocks.length-1}END`; });
  t = t.replace(/\$[^\$\n]+?\$|\\\([^\)]+?\\\)/g, m => { latexBlocks.push({type:'inline',src:m}); return `LATEXINLINE${latexBlocks.length-1}END`; });
  let html = marked.parse(t.replace(/(<[^>]+class="[^"]*(?:search-tag|src-chip)[^"]*"[\s\S]*?<\/[^>]+>)/g,'\n\n$1\n\n'));
  // Restore and render LaTeX
  html = html.replace(/LATEXBLOCK(\d+)END/g, (_,i) => {
    try { return katex.renderToString(latexBlocks[i].src.replace(/^\$\$|\$\$$|^\\\[|\\\]$/g,''), {displayMode:true,throwOnError:false}); }
    catch(e){ return latexBlocks[i].src; }
  });
  html = html.replace(/LATEXINLINE(\d+)END/g, (_,i) => {
    try { return katex.renderToString(latexBlocks[i].src.replace(/^\$|\$$|^\\\(|\\\)$/g,''), {displayMode:false,throwOnError:false}); }
    catch(e){ return latexBlocks[i].src; }
  });
  return html;
}
function esc(t){ return String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function escChat(t){ return esc(t).replace(/\n/g,'<br>'); }
function now(){ return new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'}); }

// ══════════════════════════════════════════════════════════════════════
// ARTIFACTS
// ══════════════════════════════════════════════════════════════════════
function parseArt(text){
  const m=text.match(/<artifact\s+type="([^"]+)"\s+title="([^"]*)"[^>]*>([\s\S]*?)<\/artifact>/i);
  if(!m)return null;
  return{type:m[1].toLowerCase(),title:m[2]||'Artifact',content:m[3].trim()};
}
function artStrip(t){ return t.replace(/<artifact[\s\S]*?<\/artifact>/gi,'').trim(); }
function artIcon(t){ return{html:'🌐',svg:'🎨',javascript:'⚡',css:'💅',python:'🐍',markdown:'📝',json:'📦',csv:'📊'}[t]||'📄'; }

function openArt(art){
  currentArt=art;
  document.getElementById('art-title').textContent=art.title;
  document.getElementById('art-lang').textContent=art.type;
  document.getElementById('art-panel').classList.add('open');
  document.getElementById('art-empty').style.display='none';
  artTab('preview');
}
function artTab(tab){
  document.getElementById('atab-pre').classList.toggle('active',tab==='preview');
  document.getElementById('atab-cod').classList.toggle('active',tab==='code');
  const ifrm=document.getElementById('art-iframe');
  const codeDiv=document.getElementById('art-code');
  if(tab==='preview'){
    ifrm.style.display='block'; codeDiv.style.display='none';
    if(!currentArt) return;
    let html='';
    if(currentArt.type==='html') html=currentArt.content;
    else if(currentArt.type==='svg') html=`<!DOCTYPE html><html><body style="margin:0;background:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;">${currentArt.content}</body></html>`;
    else if(currentArt.type==='markdown') html=`<!DOCTYPE html><html><head><style>body{font-family:system-ui,sans-serif;padding:32px;max-width:760px;margin:0 auto;line-height:1.7;color:#111;}h1,h2,h3{color:#1a1a2e;}code{background:#f0f0f0;padding:2px 6px;border-radius:4px;}pre{background:#1a1b26;color:#abb2bf;padding:16px;border-radius:8px;overflow-x:auto;}pre code{background:none;padding:0;}</style></head><body>${marked.parse(currentArt.content)}</body></html>`;
    else if(currentArt.type==='csv'){
      const rows=currentArt.content.trim().split('\n').map(r=>r.split(',').map(c=>c.trim().replace(/^"|"$/g,'')));
      const hdr=rows[0]; const data=rows.slice(1);
      html=`<!DOCTYPE html><html><head><style>body{font-family:system-ui,sans-serif;padding:20px;background:#fff;}table{border-collapse:collapse;width:100%;font-size:13px;}th{background:#6366f1;color:#fff;padding:8px 12px;text-align:left;}td{padding:7px 12px;border-bottom:1px solid #e5e7eb;}tr:nth-child(even){background:#f9fafb;}</style></head><body><table><thead><tr>${hdr.map(h=>`<th>${esc(h)}</th>`).join('')}</tr></thead><tbody>${data.map(r=>`<tr>${r.map(c=>`<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></body></html>`;
    }
    else html=`<!DOCTYPE html><html><head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css"><script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"><\/script></head><body style="margin:0;"><pre style="margin:0;min-height:100vh;"><code class="language-${currentArt.type}" style="display:block;padding:20px;font-size:12px;min-height:100vh;">${esc(currentArt.content)}</code></pre><script>hljs.highlightAll();<\/script></body></html>`;
    ifrm.srcdoc=html;
  } else {
    ifrm.style.display='none'; codeDiv.style.display='block';
    if(!currentArt) return;
    const cb=document.getElementById('art-code-el');
    cb.className=`language-${currentArt.type}`; cb.textContent=currentArt.content;
    hljs.highlightElement(cb);
  }
}
function artClose(){ document.getElementById('art-panel').classList.remove('open'); }
function artCopy(){ if(!currentArt)return; navigator.clipboard.writeText(currentArt.content).then(()=>showToast('📋 Copied!')); }
function artDownload(){
  if(!currentArt)return;
  const ext={html:'html',svg:'svg',javascript:'js',css:'css',python:'py',markdown:'md',json:'json',csv:'csv'}[currentArt.type]||'txt';
  const a=Object.assign(document.createElement('a'),{href:URL.createObjectURL(new Blob([currentArt.content],{type:'text/plain'})),download:`${currentArt.title.replace(/\s+/g,'-').toLowerCase()}.${ext}`});
  a.click(); URL.revokeObjectURL(a.href); showToast('⬇ Downloaded!');
}
function artFullscreen(){
  if(!currentArt)return;
  const w=window.open('','_blank');
  if(currentArt.type==='html')w.document.write(currentArt.content);
  else w.document.write(`<pre style="font-family:monospace;padding:20px;white-space:pre-wrap;background:#0d0e14;color:#abb2bf;min-height:100vh;">${esc(currentArt.content)}</pre>`);
  w.document.close();
}

// ══════════════════════════════════════════════════════════════════════
// ACTIONS
// ══════════════════════════════════════════════════════════════════════
function copyBubble(btn){ const b=btn.closest('.msg-body').querySelector('.msg-bubble'); if(!b)return; navigator.clipboard.writeText(b.innerText).then(()=>{btn.textContent='✓ Copied';setTimeout(()=>btn.textContent='📋 Copy',2000);}); }
function copyCode(btn){ navigator.clipboard.writeText(btn.closest('pre').querySelector('code').innerText).then(()=>{btn.textContent='✓'; btn.classList.add('copied');setTimeout(()=>{btn.textContent='Copy';btn.classList.remove('copied');},2000);}); }
function copyText(t){ navigator.clipboard.writeText(t).then(()=>showToast('📋 Copied!')); }

async function regen(){
  if(S.thinking)return;
  const conv=activeConv(); if(!conv)return;
  while(conv.messages.length&&conv.messages[conv.messages.length-1].role==='assistant') conv.messages.pop();
  const ais=document.getElementById('chat').querySelectorAll('.msg.ai'); if(ais.length)ais[ais.length-1].remove();
  S.thinking=true; setStatus('thinking','Regenerating...');
  const streamDiv=createStreamDiv();
  const bub=streamDiv.querySelector('.msg-bubble');
  let reply='';
  try{
    reply=await callAPI(null, chunk=>{ reply+=chunk; bub.innerHTML=renderMD(reply)+'<span class="stream-cur"></span>'; scrollBot(); });
    finaliseStream(streamDiv,reply);
    conv.messages.push({role:'assistant',content:reply.replace(/<artifact[\s\S]*?<\/artifact>/gi,'[artifact]')}); save();
    setStatus('ready','Online — ready to go');
  }catch(err){ streamDiv.remove(); renderMsg('ai',`**Error:** ${err.message}`,true); setStatus('ready','Error'); }
  S.thinking=false;
}

document.getElementById('btn-clear').addEventListener('click',()=>{ if(!msgs().length)return; if(!confirm('Clear this conversation?'))return; const c=activeConv(); if(c)c.messages=[]; save(); showWelcome(); artClose(); showToast('🗑️ Cleared'); });
document.getElementById('btn-export').addEventListener('click',()=>{
  const m=msgs(); if(!m.length){showToast('Nothing to export!');return;}
  const out=m.map(msg=>`[${msg.role.toUpperCase()}]\n${msg.content}`).join('\n\n---\n\n');
  const a=Object.assign(document.createElement('a'),{href:URL.createObjectURL(new Blob([`BAME AI Export\n${new Date().toLocaleString()}\n${'═'.repeat(50)}\n\n${out}`],{type:'text/plain'})),download:'bame-ai-chat.txt'});
  a.click(); URL.revokeObjectURL(a.href); showToast('📁 Exported!');
});

// ══════════════════════════════════════════════════════════════════════
// CONVERSATION TABS
// ══════════════════════════════════════════════════════════════════════
function renderTabs(){
  const bar=document.getElementById('conv-bar');
  const newBtn=document.getElementById('btn-new-tab');
  bar.innerHTML='';
  conversations.forEach(c=>{
    const t=document.createElement('div');
    t.className='ctab'+(c.id===activeConvId?' active':'');
    t.dataset.cid=c.id;
    t.innerHTML=`<span class="ctab-name">${esc(c.name)}</span><button class="ctab-x" onclick="closeTab(event,${c.id})">✕</button>`;
    t.addEventListener('click',e=>{ if(!e.target.classList.contains('ctab-x'))switchTab(c.id); });
    bar.appendChild(t);
  });
  bar.appendChild(newBtn);
}

function switchTab(id){
  activeConvId=id; renderTabs();
  if(msgs().length)renderAllMsgs(); else showWelcome();
}

function closeTab(e,id){
  e.stopPropagation();
  if(conversations.length===1){showToast('⚠️ Keep at least one conversation');return;}
  conversations=conversations.filter(c=>c.id!==id);
  if(activeConvId===id){ activeConvId=conversations[0].id; if(msgs().length)renderAllMsgs();else showWelcome(); }
  save(); renderTabs();
}

document.getElementById('btn-new-tab').addEventListener('click',()=>{
  const id=Date.now();
  conversations.push({id,name:'New Chat',messages:[]});
  activeConvId=id; save(); renderTabs(); showWelcome();
});

// ══════════════════════════════════════════════════════════════════════
// MEMORY
// ══════════════════════════════════════════════════════════════════════
document.getElementById('btn-memory').addEventListener('click',()=>{ document.getElementById('mem-panel').classList.add('open'); renderMemory(); });
document.getElementById('mem-close').addEventListener('click',()=>document.getElementById('mem-panel').classList.remove('open'));
document.getElementById('mem-add-btn').addEventListener('click',addMem);
document.getElementById('mem-in').addEventListener('keydown',e=>{if(e.key==='Enter')addMem();});

function addMem(){ const i=document.getElementById('mem-in'); const t=i.value.trim(); if(!t)return; memories.push({id:Date.now(),text:t,date:new Date().toLocaleDateString()}); save(); i.value=''; renderMemory(); showToast('🧠 Memory saved'); }
function delMem(id){ memories=memories.filter(m=>m.id!==id); save(); renderMemory(); }
function renderMemory(){
  const list=document.getElementById('mem-list');
  if(!memories.length){ list.innerHTML='<div class="mem-empty">No memories yet.<br>Add facts so BAME AI remembers you.</div>'; return; }
  list.innerHTML=memories.map(m=>`<div class="mem-item"><div class="mem-item-text">${esc(m.text)}</div><div class="mem-item-meta">${m.date}</div><button class="mem-item-del" onclick="delMem(${m.id})">✕</button></div>`).join('');
}

// ══════════════════════════════════════════════════════════════════════
// SETTINGS
// ══════════════════════════════════════════════════════════════════════
document.getElementById('btn-settings').addEventListener('click',()=>openModal('modal-settings'));
document.getElementById('s-cancel').addEventListener('click',()=>closeModal('modal-settings'));

// ══════════════════════════════════════════════════════════════════════
// VIBE MODAL
// ══════════════════════════════════════════════════════════════════════
document.getElementById('btn-vibe').addEventListener('click',()=>{
  setupToneGrid('modal-tone-grid',S.tone); openModal('modal-vibe');
});
document.getElementById('vibe-cancel').addEventListener('click',()=>closeModal('modal-vibe'));
document.getElementById('vibe-ok').addEventListener('click',()=>{
  const c=document.querySelector('#modal-tone-grid .tone-card.selected');
  if(c&&c.dataset.tone!==S.tone){ S.tone=c.dataset.tone; save(); updateToneUI(); showToast(`Vibe → ${TONES[S.tone].label} ${TONES[S.tone].emoji}`); }
  closeModal('modal-vibe');
});

// ══════════════════════════════════════════════════════════════════════
// RESEARCH MODAL
// ══════════════════════════════════════════════════════════════════════
document.getElementById('btn-research').addEventListener('click',()=>{ document.getElementById('research-q').value=''; openModal('modal-research'); });
document.getElementById('research-cancel').addEventListener('click',()=>closeModal('modal-research'));
document.querySelectorAll('#modal-research .picker-btn').forEach(b=>{ b.addEventListener('click',()=>{ document.querySelectorAll('#modal-research .picker-btn').forEach(x=>x.classList.remove('sel')); b.classList.add('sel'); researchDepth=b.dataset.depth; }); });
document.getElementById('research-go').addEventListener('click',async()=>{
  const q=document.getElementById('research-q').value.trim();
  if(!q){showToast('⚠️ Enter a research topic');return;}
  closeModal('modal-research');
  await runResearch(q, researchDepth);
});

// ══════════════════════════════════════════════════════════════════════
// IMAGE GEN MODAL
// ══════════════════════════════════════════════════════════════════════
document.getElementById('btn-imggen').addEventListener('click',()=>{ document.getElementById('img-prompt').value=''; openModal('modal-imggen'); });
document.getElementById('imggen-cancel').addEventListener('click',()=>closeModal('modal-imggen'));
document.querySelectorAll('#style-chips .chip').forEach(c=>{ c.addEventListener('click',()=>{ document.querySelectorAll('#style-chips .chip').forEach(x=>x.classList.remove('sel')); c.classList.add('sel'); imgStyle=c.dataset.style; }); });
document.querySelectorAll('#modal-imggen .picker-btn').forEach(b=>{ b.addEventListener('click',()=>{ document.querySelectorAll('#modal-imggen .picker-btn').forEach(x=>x.classList.remove('sel')); b.classList.add('sel'); imgSize=b.dataset.size; }); });
document.getElementById('imggen-go').addEventListener('click',async()=>{
  const p=document.getElementById('img-prompt').value.trim();
  if(!p){showToast('⚠️ Describe the image');return;}
  closeModal('modal-imggen');
  await generateImage(p);
});

// ══════════════════════════════════════════════════════════════════════
// CODE MODAL
// ══════════════════════════════════════════════════════════════════════
document.getElementById('btn-code').addEventListener('click',()=>openModal('modal-code'));

// ══════════════════════════════════════════════════════════════════════
// MODAL UTILS
// ══════════════════════════════════════════════════════════════════════
function openModal(id){ document.getElementById(id).classList.add('open'); }
function closeModal(id){ document.getElementById(id).classList.remove('open'); }
document.querySelectorAll('.overlay').forEach(o=>{ o.addEventListener('click',e=>{ if(e.target===o)o.classList.remove('open'); }); });

// ══════════════════════════════════════════════════════════════════════
// WELCOME + SCROLL
// ══════════════════════════════════════════════════════════════════════
function showWelcome(){
  document.getElementById('chat').innerHTML=`
    <div id="welcome">
      <div class="wlc-logo">B</div>
      <div class="wlc-title">What can <span>BAME AI</span> do?</div>
      <div class="wlc-sub">Research agent · Streaming · PDF analysis · Image gen · Code interpreter · Web scraping · Memory</div>
      <div class="cap-chips">
        <span class="cap-chip">🔬 Deep Research</span><span class="cap-chip">⚡ Streaming</span>
        <span class="cap-chip">📄 PDF/Docs</span><span class="cap-chip">🎨 Image Gen</span>
        <span class="cap-chip">🌐 Web Scraping</span><span class="cap-chip">🧑‍💻 Code Runner</span>
        <span class="cap-chip">🧠 Memory</span><span class="cap-chip">📊 Data Analysis</span>
        <span class="cap-chip">🎤 Voice Input</span><span class="cap-chip">💬 Multi-Tabs</span>
      </div>
      <div class="starters">
        <div class="starter" onclick="fillInput(this)"><span class="starter-ic">🎮</span>Build a playable Snake game with scoring</div>
        <div class="starter" onclick="fillInput(this)"><span class="starter-ic">🔬</span>Research the latest in quantum computing</div>
        <div class="starter" onclick="fillInput(this)"><span class="starter-ic">📊</span>Create an interactive global GDP dashboard</div>
        <div class="starter" onclick="fillInput(this)"><span class="starter-ic">🌐</span>Scrape and summarise https://news.ycombinator.com</div>
      </div>
    </div>`;
}
function fillInput(el){ const t=el.innerText.replace(/^[^\w]*/,'').trim(); ta.value=t; autoResize(); sendBtn.disabled=false; ta.focus(); }

const chatEl=document.getElementById('chat');
chatEl.addEventListener('scroll',()=>{ const a=chatEl.scrollHeight-chatEl.scrollTop-chatEl.clientHeight<80; document.getElementById('scroll-btn').classList.toggle('show',!a&&chatEl.scrollHeight>chatEl.clientHeight+200); });
function scrollBot(){ chatEl.scrollTo({top:chatEl.scrollHeight,behavior:'smooth'}); }

let toastT; function showToast(m){ const t=document.getElementById('toast'); t.textContent=m; t.classList.add('show'); clearTimeout(toastT); toastT=setTimeout(()=>t.classList.remove('show'),2600); }
function setStatus(type,text){ document.getElementById('sdot').className='sdot'+(type==='thinking'?' thinking':''); document.getElementById('stext').textContent=text; }
function updateToneUI(){ document.getElementById('tone-badge').textContent=S.tone; document.getElementById('tone-emoji').textContent=TONES[S.tone].emoji; }

function setupToneGrid(gid,active){ document.querySelectorAll(`#${gid} .tone-card`).forEach(c=>{ c.classList.toggle('selected',c.dataset.tone===active); c.addEventListener('click',()=>{ document.querySelectorAll(`#${gid} .tone-card`).forEach(x=>x.classList.remove('selected')); c.classList.add('selected'); }); }); }

// ══════════════════════════════════════════════════════════════════════
// ONBOARDING
// ══════════════════════════════════════════════════════════════════════
const ob=document.getElementById('onboarding');
const app=document.getElementById('app');

setupToneGrid('ob-tone-grid', S.tone);

document.getElementById('ob-launch').addEventListener('click',()=>{
  const tc=document.querySelector('#ob-tone-grid .tone-card.selected');
  S.tone=tc?tc.dataset.tone:'witty';
  save(); launchApp();
});

function launchApp(){
  ob.classList.add('hidden');
  setTimeout(()=>{
    ob.style.display='none'; app.classList.add('visible');
    updateToneUI(); renderTabs(); renderMemory();
    if(msgs().length)renderAllMsgs(); else showWelcome();
  },500);
}
setTimeout(launchApp, 80);

// ══════════════════════════════════════════════════════════════════════
// KEYBOARD SHORTCUTS
// ══════════════════════════════════════════════════════════════════════
document.addEventListener('keydown',e=>{
  if((e.ctrlKey||e.metaKey)&&e.key==='k'){ e.preventDefault(); ta.focus(); }
  if((e.ctrlKey||e.metaKey)&&!e.shiftKey&&e.key==='t'&&document.getElementById('app').classList.contains('visible')){ e.preventDefault(); document.getElementById('btn-new-tab').click(); }
  if((e.ctrlKey||e.metaKey)&&e.shiftKey&&e.key==='R'){ e.preventDefault(); document.getElementById('btn-research').click(); }
  if((e.ctrlKey||e.metaKey)&&e.shiftKey&&e.key==='I'){ e.preventDefault(); document.getElementById('btn-code').click(); }
  if(e.key==='Escape'){
    document.querySelectorAll('.overlay.open').forEach(m=>m.classList.remove('open'));
    document.getElementById('mem-panel').classList.remove('open');
    if(isRec)stopRec();
  }
});

// ══════════════════════════════════════════════════════════════════════
// LOAD CHART.JS (for data analysis in artifacts)
// ══════════════════════════════════════════════════════════════════════
(()=>{ const s=document.createElement('script'); s.src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js'; document.head.appendChild(s); })();

// ══════════════════════════════════════════════════════════════════════
// AUTO-HIDE NAVBAR
// ══════════════════════════════════════════════════════════════════════
(()=>{
  const hdr = document.querySelector('.site-header');
  if(!hdr) return;
  hdr.style.cssText += 'position:fixed;top:0;left:0;right:0;transform:translateY(-100%);transition:transform 0.25s ease;z-index:99999;';
  // Invisible hover trigger zone at the top of the screen
  const trigger = document.createElement('div');
  trigger.style.cssText = 'position:fixed;top:0;left:0;right:0;height:8px;z-index:100000;';
  document.body.appendChild(trigger);
  trigger.addEventListener('mouseenter', ()=> hdr.style.transform='translateY(0)');
  hdr.addEventListener('mouseleave', ()=> hdr.style.transform='translateY(-100%)');
})();
</script>
