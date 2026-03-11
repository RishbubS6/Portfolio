---
permalink: /hardest
--- 

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>V.O.I.D.EXE — The World's Hardest Game</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&display=swap');

  :root {
    --neon-cyan: #00fff9;
    --neon-pink: #ff006e;
    --neon-yellow: #ffee00;
    --neon-green: #39ff14;
    --bg: #030308;
    --grid: #0a0a1a;
    --wall: #0d0d2b;
    --wall-border: #1a1a4e;
    --player: #00fff9;
    --enemy: #ff006e;
    --goal: #39ff14;
    --coin: #ffee00;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--neon-cyan);
    font-family: 'Share Tech Mono', monospace;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    overflow: hidden;
    user-select: none;
  }

  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
      repeating-linear-gradient(0deg, transparent, transparent 39px, rgba(0,255,249,0.03) 40px),
      repeating-linear-gradient(90deg, transparent, transparent 39px, rgba(0,255,249,0.03) 40px);
    pointer-events: none;
    z-index: 0;
  }

  #wrapper {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 14px;
  }

  #title {
    font-family: 'Orbitron', monospace;
    font-size: 2.2rem;
    font-weight: 900;
    letter-spacing: 0.18em;
    color: var(--neon-cyan);
    text-shadow:
      0 0 10px var(--neon-cyan),
      0 0 30px var(--neon-cyan),
      0 0 60px rgba(0,255,249,0.4);
    animation: flicker 4s infinite;
  }

  @keyframes flicker {
    0%,95%,100% { opacity: 1; }
    96% { opacity: 0.7; }
    97% { opacity: 1; }
    98% { opacity: 0.5; }
    99% { opacity: 1; }
  }

  #hud {
    display: flex;
    gap: 40px;
    font-size: 0.85rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  .hud-item span {
    color: var(--neon-yellow);
    font-size: 1.1rem;
    font-family: 'Orbitron', monospace;
    text-shadow: 0 0 8px var(--neon-yellow);
  }

  #canvas-wrap {
    position: relative;
    border: 1px solid rgba(0,255,249,0.3);
    box-shadow:
      0 0 20px rgba(0,255,249,0.15),
      0 0 60px rgba(0,255,249,0.05),
      inset 0 0 30px rgba(0,0,0,0.8);
  }

  canvas { display: block; }

  #overlay {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: rgba(3,3,8,0.92);
    backdrop-filter: blur(4px);
    gap: 18px;
    transition: opacity 0.3s;
  }

  #overlay.hidden { display: none; }

  #overlay-title {
    font-family: 'Orbitron', monospace;
    font-size: 2.4rem;
    font-weight: 900;
    text-align: center;
    line-height: 1.2;
  }

  #overlay-title.cyan {
    color: var(--neon-cyan);
    text-shadow: 0 0 20px var(--neon-cyan), 0 0 50px rgba(0,255,249,0.5);
  }
  #overlay-title.pink {
    color: var(--neon-pink);
    text-shadow: 0 0 20px var(--neon-pink), 0 0 50px rgba(255,0,110,0.5);
  }
  #overlay-title.green {
    color: var(--neon-green);
    text-shadow: 0 0 20px var(--neon-green), 0 0 50px rgba(57,255,20,0.5);
  }

  #overlay-sub {
    font-size: 0.9rem;
    color: rgba(0,255,249,0.6);
    letter-spacing: 0.15em;
    text-align: center;
    line-height: 1.7;
  }

  #start-btn {
    margin-top: 8px;
    padding: 12px 40px;
    font-family: 'Orbitron', monospace;
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    background: transparent;
    color: var(--neon-cyan);
    border: 1px solid var(--neon-cyan);
    cursor: pointer;
    text-transform: uppercase;
    position: relative;
    overflow: hidden;
    transition: all 0.2s;
    box-shadow: 0 0 15px rgba(0,255,249,0.3), inset 0 0 15px rgba(0,255,249,0.05);
  }

  #start-btn:hover {
    background: rgba(0,255,249,0.1);
    box-shadow: 0 0 30px rgba(0,255,249,0.6), inset 0 0 20px rgba(0,255,249,0.1);
    transform: scale(1.03);
  }

  #controls-hint {
    font-size: 0.72rem;
    color: rgba(0,255,249,0.35);
    letter-spacing: 0.12em;
    text-align: center;
  }

  .scanline {
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 100vh;
    background: linear-gradient(transparent 50%, rgba(0,0,0,0.03) 50%);
    background-size: 100% 4px;
    pointer-events: none;
    z-index: 100;
    animation: scan 8s linear infinite;
    opacity: 0.4;
  }

  @keyframes scan {
    0% { background-position: 0 0; }
    100% { background-position: 0 100vh; }
  }
  #cs-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(0,255,249,0.15);
    padding-bottom: 14px;
    margin-bottom: 4px;
  }
  #cs-title-tag {
    font-family: 'Orbitron', monospace;
    font-size: 0.8rem;
    font-weight: 900;
    letter-spacing: 0.25em;
    color: var(--neon-cyan);
    text-shadow: 0 0 10px var(--neon-cyan);
  }
  #cs-counter {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    color: rgba(0,255,249,0.35);
    letter-spacing: 0.1em;
  }

  /* ── CUTSCENE ─────────────────────────────────────────── */
  #cutscene {
    position: fixed;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    background: rgba(0,0,0,0.96);
    transition: opacity 0.6s;
  }
  #cutscene.hidden { display: none; }
  #cutscene.fade-out { opacity: 0; pointer-events: none; }

  #cs-bg {
    position: absolute;
    inset: 0;
    background:
      repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(0,255,249,0.015) 4px);
    pointer-events: none;
  }

  #cs-content {
    position: relative;
    z-index: 2;
    width: min(680px, 90vw);
    padding: 40px 48px;
    border: 1px solid rgba(0,255,249,0.3);
    background: rgba(3,3,20,0.98);
    box-shadow: 0 0 60px rgba(0,255,249,0.12), 0 0 120px rgba(0,255,249,0.04), inset 0 0 30px rgba(0,0,0,0.6);
    display: flex;
    flex-direction: column;
    gap: 22px;
  }

  #cs-label {
    font-family: 'Orbitron', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.3em;
    color: var(--neon-pink);
    text-shadow: 0 0 8px var(--neon-pink);
    text-transform: uppercase;
    min-height: 14px;
  }

  #cs-text {
    font-family: 'Share Tech Mono', monospace;
    font-size: 1rem;
    line-height: 1.9;
    color: rgba(0,255,249,0.9);
    min-height: 160px;
    white-space: pre-wrap;
  }

  #cs-text .highlight { color: var(--neon-yellow); text-shadow: 0 0 6px var(--neon-yellow); }
  #cs-text .danger    { color: var(--neon-pink);   text-shadow: 0 0 6px var(--neon-pink); }
  #cs-text .success   { color: var(--neon-green);  text-shadow: 0 0 8px var(--neon-green); }

  #cs-btn {
    align-self: flex-end;
    padding: 8px 24px;
    font-family: 'Orbitron', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    background: transparent;
    color: var(--neon-cyan);
    border: 1px solid rgba(0,255,249,0.4);
    cursor: pointer;
    opacity: 0;
    transition: opacity 0.3s, box-shadow 0.2s;
    pointer-events: none;
  }
  #cs-btn.visible {
    opacity: 1;
    pointer-events: all;
  }
  #cs-btn:hover {
    box-shadow: 0 0 16px rgba(0,255,249,0.4);
    background: rgba(0,255,249,0.07);
  }

  /* glitch flicker on reveal */
  @keyframes glitch {
    0%,100% { transform: none; filter: none; }
    20% { transform: translateX(-2px); filter: hue-rotate(90deg); }
    40% { transform: translateX(2px);  filter: hue-rotate(-90deg); }
    60% { transform: none; filter: brightness(2); }
    80% { transform: translateX(-1px); filter: none; }
  }
  .glitch-anim { animation: glitch 0.4s steps(1) 1; }
</style>
</head>
<body>
<div class="scanline"></div>

<!-- CUTSCENE — fixed full-screen overlay, sits above everything -->
<div id="cutscene" class="hidden">
  <div id="cs-bg"></div>
  <div id="cs-content">
    <div id="cs-header">
      <span id="cs-title-tag">V.O.I.D.EXE</span>
      <span id="cs-counter"></span>
    </div>
    <div id="cs-label"></div>
    <div id="cs-text"></div>
    <button id="cs-btn">[ CONTINUE ]</button>
  </div>
</div>
<div id="wrapper">
  <div id="title">V.O.I.D.EXE</div>
  <div id="hud">
    <div class="hud-item">LEVEL <span id="h-level">1</span></div>
    <div class="hud-item">DEATHS <span id="h-deaths">0</span></div>
    <div class="hud-item">COINS <span id="h-coins">0</span>/<span id="h-total">0</span></div>
  </div>
  <div id="canvas-wrap">
    <canvas id="c"></canvas>
    <div id="overlay">
      <div id="overlay-title" class="cyan">V.O.I.D.EXE</div>
      <div id="overlay-sub">
        Navigate the grid.<br>
        Collect all coins.<br>
        Reach the green zone.<br>
        Don't touch the red.
      </div>
      <button id="start-btn" onclick="startGame()">INITIALIZE</button>
      <div id="controls-hint">WASD / ARROW KEYS — MOVE &nbsp;|&nbsp; Z — SKIP LEVEL</div>
    </div>

    <!-- CUTSCENE OVERLAY — full page, outside canvas-wrap -->
  </div>
</div>

<script>
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');

const CELL = 32;
const COLS = 22;
const ROWS = 16;
const W = COLS * CELL;
const H = ROWS * CELL;
canvas.width = W;
canvas.height = H;

// ─── LEVELS ───────────────────────────────────────────────────────────────────
// Each level: walls (grid cells), start, goal zone, coins, enemies
const LEVELS = [
  // ── Level 1 — Two pillars ──────────────────────────────────────────────────
  // Left pillar : cols 5–6, rows 2–13
  // Right pillar: cols 15–16, rows 2–13
  // Three lanes: LEFT cols 1–4, MIDDLE cols 7–14, RIGHT cols 17–20
  // All lanes fully open top-to-bottom. Player starts left lane, goal right lane.
  {
    walls: buildBorderWalls(COLS, ROWS).concat([
      ...rectWall(5,2,2,12),   // left pillar  cols 5-6, rows 2-13
      ...rectWall(15,2,2,12),  // right pillar cols 15-16, rows 2-13
    ]),
    start: {x:2, y:7},
    goal:  {x:18, y:5, w:3, h:6},  // cols 18-20, rows 5-10 — right lane, open
    coins: [
      // middle lane coins — cols 7-14, all rows open
      {x:8, y:3}, {x:11,y:3}, {x:13,y:3},
      {x:8, y:12},{x:11,y:12},{x:13,y:12},
      {x:10,y:7},
    ],
    enemies: [
      // left lane vertical patrol (col 2, fully open)
      {x:2*CELL+CELL/2, y:3*CELL+CELL/2,  vx:0,  vy:4.8, ax:0, ay:0},
      {x:2*CELL+CELL/2, y:11*CELL+CELL/2, vx:0,  vy:-4.8,ax:0, ay:0},
      // middle lane horizontal patrol (row 7, cols 7-14 open)
      {x:8*CELL+CELL/2, y:7*CELL+CELL/2,  vx:4.8,vy:0,   ax:0, ay:0},
      // right lane vertical patrol (col 19, fully open)
      {x:19*CELL+CELL/2,y:5*CELL+CELL/2,  vx:0,  vy:4.8, ax:0, ay:0},
    ]
  },

  // ── Level 2 — Open cross corridor ─────────────────────────────────────────
  // A plus-sign of open corridors. Walls fill the four corner quadrants.
  // Horizontal corridor: row 6-9, cols 1-20 (fully open)
  // Vertical corridor  : col 9-12, rows 1-14 (fully open)
  // Four corner blocks: e.g. top-left = cols 1-8, rows 1-5
  // Entry from left at start (col 1, row 7), goal at far right (cols 18-20, rows 6-9)
  {
    walls: buildBorderWalls(COLS, ROWS).concat([
      ...rectWall(1,1,8,5),    // top-left block     cols 1-8,   rows 1-5
      ...rectWall(13,1,8,5),   // top-right block    cols 13-20, rows 1-5
      ...rectWall(1,10,8,5),   // bottom-left block  cols 1-8,   rows 10-14
      ...rectWall(13,10,8,5),  // bottom-right block cols 13-20, rows 10-14
    ]),
    start: {x:1, y:7},
    goal:  {x:18, y:6, w:2, h:4},  // cols 18-19 rows 6-9 — horizontal corridor, open
    coins: [
      // horizontal corridor (row 7, cols 2-17 open between corner blocks)
      {x:3, y:7}, {x:6, y:7}, {x:15,y:7}, {x:17,y:7},
      // vertical corridor (col 10, rows 2-9 and rows 10-13 open)
      {x:10,y:2}, {x:10,y:4}, {x:10,y:11},{x:10,y:13},
    ],
    enemies: [
      // horizontal corridor sweepers
      {x:3*CELL+CELL/2,  y:7*CELL+CELL/2,  vx:4.8, vy:0,   ax:0, ay:0},
      {x:16*CELL+CELL/2, y:7*CELL+CELL/2,  vx:-4.8,vy:0,   ax:0, ay:0},
      // vertical corridor sweepers
      {x:10*CELL+CELL/2, y:2*CELL+CELL/2,  vx:0,   vy:4.8, ax:0, ay:0},
      {x:10*CELL+CELL/2, y:12*CELL+CELL/2, vx:0,   vy:-4.8,ax:0, ay:0},
      // intersection orbiter — diagonal bounce within cross centre (cols 9-12, rows 6-9)
      {x:9*CELL+CELL/2,  y:6*CELL+CELL/2,  vx:3.4, vy:3.4, ax:0, ay:0, bounce:true},
    ]
  },

  // ── Level 3 — Snake maze (alternating-gap slabs) ──────────────────────────
  // Four slabs, alternating gap top / gap bottom.
  // Slab A: cols 4-5, rows 1-10  → gap BELOW (rows 11-14), player goes UNDER
  // Slab B: cols 8-9, rows 4-14  → gap ABOVE (rows 1-3),   player goes OVER
  // Slab C: cols 12-13, rows 1-10 → gap BELOW (rows 11-14), player goes UNDER
  // Slab D: cols 16-17, rows 4-14 → gap ABOVE (rows 1-3),   player goes OVER
  // Coins placed ONLY in corridor sections accessible via the gaps
  // Goal: cols 19-20, rows 1-4 (top-right, reachable via gap above slab D)
  {
    walls: buildBorderWalls(COLS, ROWS).concat([
      ...rectWall(4,1,2,10),   // slab A: cols 4-5, rows 1-10
      ...rectWall(8,4,2,11),   // slab B: cols 8-9, rows 4-14
      ...rectWall(12,1,2,10),  // slab C: cols 12-13, rows 1-10
      ...rectWall(16,4,2,11),  // slab D: cols 16-17, rows 4-14
    ]),
    start: {x:2, y:7},
    goal:  {x:19, y:1, w:2, h:4},  // cols 19-20, rows 1-4 — above slab D, open
    coins: [
      // corridor 1 (cols 1-3): fully open, coins top and bottom
      {x:2, y:3},  {x:2, y:12},
      // corridor 2 (cols 6-7): open; gap under slab A connects bottom, gap over slab B connects top
      {x:6, y:2},  {x:6, y:12},
      // corridor 3 (cols 10-11): symmetric to corridor 1
      {x:10,y:3},  {x:10,y:12},
      // corridor 4 (cols 14-15): gap under slab C connects bottom, gap over slab D connects top
      {x:14,y:2},  {x:14,y:12},
      // corridor 5 (cols 18-20): above slab D gap — rows 1-3 open
      {x:19,y:2},  {x:19,y:8},
    ],
    enemies: [
      // each enemy vertical-patrols its own corridor (all verified open)
      {x:2*CELL+CELL/2,  y:3*CELL+CELL/2,  vx:0, vy:4.8,  ax:0, ay:0},
      {x:6*CELL+CELL/2,  y:12*CELL+CELL/2, vx:0, vy:-4.8, ax:0, ay:0},
      {x:10*CELL+CELL/2, y:3*CELL+CELL/2,  vx:0, vy:4.8,  ax:0, ay:0},
      {x:14*CELL+CELL/2, y:12*CELL+CELL/2, vx:0, vy:-4.8, ax:0, ay:0},
      {x:19*CELL+CELL/2, y:2*CELL+CELL/2,  vx:0, vy:4.8,  ax:0, ay:0},
    ]
  },

  // ── Level 4 — Gauntlet (fence posts) ──────────────────────────────────────
  // Vertical posts every 3 cols. Top posts rows 2-6, bottom posts rows 9-13.
  // Gap rows 7-8 lets player pass horizontally through all posts.
  // Enemies patrol the open BETWEEN-post columns vertically.
  // Coins in the gap row AND in the pockets (between posts, above/below gap).
  // Goal: cols 19-20, rows 6-9 (right end, past all posts, open).
  // Posts at cols 3,6,9,12,15,18. Between-post open cols: 1-2, 4-5, 7-8, 10-11, 13-14, 16-17, 19-20.
  {
    walls: buildBorderWalls(COLS, ROWS).concat([
      ...rectWall(3,2,1,5),  ...rectWall(6,2,1,5),  ...rectWall(9,2,1,5),
      ...rectWall(12,2,1,5), ...rectWall(15,2,1,5), ...rectWall(18,2,1,5),
      ...rectWall(3,9,1,5),  ...rectWall(6,9,1,5),  ...rectWall(9,9,1,5),
      ...rectWall(12,9,1,5), ...rectWall(15,9,1,5), ...rectWall(18,9,1,5),
    ]),
    start: {x:1, y:7},
    goal:  {x:19, y:6, w:2, h:4},
    coins: [
      // gap row — between-post cols only (NOT on post cols 3,6,9,12,15,18)
      {x:2,y:7},{x:5,y:7},{x:8,y:7},{x:11,y:7},{x:14,y:7},{x:17,y:7},
      // upper pockets (between posts, rows 3-6 — post cols excluded)
      {x:2,y:4},{x:5,y:4},{x:8,y:4},{x:11,y:4},{x:14,y:4},
      // lower pockets
      {x:2,y:11},{x:5,y:11},{x:8,y:11},{x:11,y:11},{x:14,y:11},
    ],
    enemies: [
      // vertical patrol in between-post cols (2,5,8,11,14,17) — no post walls there
      {x:2*CELL+CELL/2,  y:3*CELL+CELL/2,  vx:0,  vy:4.8,  ax:0, ay:0},
      {x:5*CELL+CELL/2,  y:12*CELL+CELL/2, vx:0,  vy:-4.8, ax:0, ay:0},
      {x:8*CELL+CELL/2,  y:3*CELL+CELL/2,  vx:0,  vy:4.8,  ax:0, ay:0},
      {x:11*CELL+CELL/2, y:12*CELL+CELL/2, vx:0,  vy:-4.8, ax:0, ay:0},
      {x:14*CELL+CELL/2, y:3*CELL+CELL/2,  vx:0,  vy:4.8,  ax:0, ay:0},
      {x:17*CELL+CELL/2, y:12*CELL+CELL/2, vx:0,  vy:-4.8, ax:0, ay:0},
      // horizontal sweeper in gap row (rows 7, full width open)
      {x:2*CELL+CELL/2,  y:7*CELL+CELL/2,  vx:4.8,vy:0,    ax:0, ay:0},
    ]
  },

  // ── Level 5 — Nested rings (3-layer onion) ────────────────────────────────
  // DESIGN PRINCIPLE: each ring has exactly ONE gap, alternating sides LEFT/RIGHT/LEFT.
  // Enemies are placed INSIDE each ring zone and cannot escape through gaps because
  // their patrol axis is perpendicular to the gap (they patrol the ring corridors, not straight
  // through the gap).
  //
  // OUTER ring walls (perimeter of cols 2-19, rows 2-13):
  //   top row 2 cols 2-19, bottom row 13 cols 2-19
  //   left  col 2 rows 3-6 + rows 9-12  (GAP at rows 7-8 LEFT side)
  //   right col 19 rows 3-12            (solid)
  //
  // MIDDLE ring walls (perimeter of cols 5-16, rows 4-11):
  //   top row 4 cols 5-16, bottom row 11 cols 5-16
  //   left  col 5 rows 5-10             (solid)
  //   right col 16 rows 5-7 + rows 9-10 (GAP at row 8 RIGHT side — 1 row gap)
  //   → use 2-row gap: col 16 rows 5-6 + rows 9-10, gap rows 7-8
  //
  // INNER ring walls (perimeter of cols 7-14, rows 6-9):
  //   top row 6 cols 7-14, bottom row 9 cols 7-14
  //   left  col 7 rows 7-8              (GAP — no wall, entry from left)
  //   right col 14 rows 7-8             (solid)
  //
  // Goal: cols 9-12, rows 7-8 (centre, inside inner ring)
  //
  // ENEMIES: placed in their ring zone, patrolling VERTICALLY so they bounce within
  // their ring and never escape through the horizontal gap.
  {
    walls: buildBorderWalls(COLS, ROWS).concat([
      // outer ring top + bottom
      ...rectWall(2,2,18,1),  ...rectWall(2,13,18,1),
      // outer ring left side with gap rows 7-8
      ...rectWall(2,3,1,4),   ...rectWall(2,9,1,4),
      // outer ring right side solid
      ...rectWall(19,3,1,10),
      // middle ring top + bottom
      ...rectWall(5,4,12,1),  ...rectWall(5,11,12,1),
      // middle ring left side solid
      ...rectWall(5,5,1,6),
      // middle ring right side with gap rows 7-8
      ...rectWall(16,5,1,2),  ...rectWall(16,9,1,2),
      // inner ring top + bottom
      ...rectWall(7,6,8,1),   ...rectWall(7,9,8,1),
      // inner ring left side: GAP rows 7-8 so NO wall at col 7 rows 7-8
      // inner ring right side solid
      ...rectWall(14,7,1,2),
    ]),
    start: {x:1, y:7},
    goal:  {x:9, y:7, w:4, h:2},
    coins: [
      // outer zone — col 10 enemy patrols vertically so move those coins off col 10
      {x:3, y:3},  {x:12,y:3},  {x:18,y:3},
      {x:3, y:12}, {x:12,y:12}, {x:18,y:12},
      // middle zone — kept clear of all enemy paths
      {x:8, y:5},  {x:12,y:5},  {x:15,y:5},
      {x:8, y:10}, {x:12,y:10}, {x:15,y:10},
    ],
    enemies: [
      // outer zone: two vertical patrollers in RIGHT half of outer zone
      {x:10*CELL+CELL/2, y:3*CELL+CELL/2,  vx:0,   vy:4.8,  ax:0, ay:0},
      {x:17*CELL+CELL/2, y:11*CELL+CELL/2, vx:0,   vy:-4.8, ax:0, ay:0},
      // outer zone: one horizontal patroller in TOP strip
      {x:4*CELL+CELL/2,  y:3*CELL+CELL/2,  vx:4.8, vy:0,    ax:0, ay:0},
      // middle zone: vertical patrol in col 10 rows 5-10 (col 10 is outside inner ring top at row 6 only for cols 7-14... col 10 row 5 is open, row 6 is inner ring top wall so enemy bounces rows 5-5... use col 6 but start at row 7 centre so it doesn't land on coins at row 5/10)
      {x:6*CELL+CELL/2,  y:7*CELL+CELL/2,  vx:0,    vy:4.8,  ax:0, ay:0},
      // inner zone: horizontal patrol inside inner ring (cols 8-13, rows 7-8)
      {x:8*CELL+CELL/2,  y:7*CELL+CELL/2,  vx:4.8,  vy:0,    ax:0, ay:0},
    ]
  }
];

function buildBorderWalls(cols, rows) {
  const w = [];
  for (let x = 0; x < cols; x++) { w.push({x,y:0}); w.push({x,y:rows-1}); }
  for (let y = 1; y < rows-1; y++) { w.push({x:0,y}); w.push({x:cols-1,y}); }
  return w;
}
function rectWall(x,y,w,h) {
  const cells = [];
  for (let row = y; row < y+h; row++)
    for (let col = x; col < x+w; col++)
      cells.push({x:col, y:row});
  return cells;
}

// ─── STATE ────────────────────────────────────────────────────────────────────
let level = 0, deaths = 0, totalCoins = 0;
let player, enemies, coins, wallSet, goalRect;
let keys = {}, dead = false, won = false, levelWon = false;
let deathTimer = 0, winFlash = 0;
let running = false;
let particles = [];

function buildWallSet(walls) {
  return new Set(walls.map(w => `${w.x},${w.y}`));
}

function initLevel(idx) {
  const L = LEVELS[idx];
  wallSet = buildWallSet(L.walls);
  player = {
    x: L.start.x * CELL + CELL/2,
    y: L.start.y * CELL + CELL/2,
    r: 10,
    trail: []
  };
  goalRect = {
    x: L.goal.x * CELL, y: L.goal.y * CELL,
    w: L.goal.w * CELL, h: L.goal.h * CELL
  };
  coins = L.coins.map(c => ({
    x: c.x * CELL + CELL/2,
    y: c.y * CELL + CELL/2,
    r: 6,
    collected: false,
    pulse: Math.random()*Math.PI*2
  }));
  enemies = L.enemies.map(e => ({...e, r: 10, startX: e.x, startY: e.y}));
  dead = false; levelWon = false; deathTimer = 0; winFlash = 0;
  document.getElementById('h-level').textContent = idx+1;
  document.getElementById('h-total').textContent = coins.length;
  updateHUD();
}

function updateHUD() {
  document.getElementById('h-deaths').textContent = deaths;
  document.getElementById('h-coins').textContent = coins.filter(c=>c.collected).length;
}

function spawnParticles(x, y, color, count=18) {
  for (let i = 0; i < count; i++) {
    const angle = (Math.PI*2/count)*i + Math.random()*0.4;
    const speed = 2 + Math.random()*4;
    particles.push({
      x, y,
      vx: Math.cos(angle)*speed,
      vy: Math.sin(angle)*speed,
      life: 1,
      color,
      r: 2+Math.random()*3
    });
  }
}

function isWall(x, y) {
  const cx = Math.floor(x / CELL);
  const cy = Math.floor(y / CELL);
  return wallSet.has(`${cx},${cy}`);
}

function movePlayer(dt) {
  if (dead || levelWon) return;
  const speed = 3.2;
  let dx = 0, dy = 0;
  if (keys['ArrowLeft']  || keys['a'] || keys['A']) dx -= speed;
  if (keys['ArrowRight'] || keys['d'] || keys['D']) dx += speed;
  if (keys['ArrowUp']    || keys['w'] || keys['W']) dy -= speed;
  if (keys['ArrowDown']  || keys['s'] || keys['S']) dy += speed;

  // Normalize diagonal
  if (dx && dy) { dx *= 0.707; dy *= 0.707; }

  const r = player.r - 1;
  // X movement
  let nx = player.x + dx;
  if (!isWall(nx - r, player.y) && !isWall(nx + r, player.y) &&
      !isWall(nx - r, player.y - r) && !isWall(nx + r, player.y - r) &&
      !isWall(nx - r, player.y + r) && !isWall(nx + r, player.y + r))
    player.x = nx;

  // Y movement
  let ny = player.y + dy;
  if (!isWall(player.x, ny - r) && !isWall(player.x, ny + r) &&
      !isWall(player.x - r, ny) && !isWall(player.x + r, ny) &&
      !isWall(player.x - r, ny - r) && !isWall(player.x + r, ny + r))
    player.y = ny;

  // Trail
  player.trail.push({x: player.x, y: player.y});
  if (player.trail.length > 18) player.trail.shift();
}

function moveEnemies() {
  if (levelWon) return;
  const L = LEVELS[level];
  enemies.forEach((e, i) => {
    const orig = L.enemies[i];

    if (orig.bounce) {
      // Bouncing enemies
      e.x += e.vx;
      e.y += e.vy;
      const r = e.r;
      if (isWall(e.x - r, e.y) || isWall(e.x + r, e.y)) e.vx *= -1;
      if (isWall(e.x, e.y - r) || isWall(e.x, e.y + r)) e.vy *= -1;
      // clamp
      e.x += e.vx * 0.1;
      e.y += e.vy * 0.1;
    } else if (orig.vx !== 0) {
      // Horizontal patrol — reverse at walls or edge
      e.x += e.vx;
      const r = e.r;
      if (isWall(e.x - r, e.y) || isWall(e.x + r, e.y) ||
          isWall(e.x - r, e.y - r) || isWall(e.x + r, e.y - r)) {
        e.vx *= -1;
        e.x += e.vx * 2;
      }
    } else {
      // Vertical patrol
      e.y += e.vy;
      const r = e.r;
      if (isWall(e.x, e.y - r) || isWall(e.x, e.y + r) ||
          isWall(e.x - r, e.y - r) || isWall(e.x + r, e.y - r)) {
        e.vy *= -1;
        e.y += e.vy * 2;
      }
    }
  });
}

function checkCollisions() {
  if (dead || levelWon) return;

  // Enemy collision
  for (const e of enemies) {
    const dx = player.x - e.x;
    const dy = player.y - e.y;
    if (Math.sqrt(dx*dx+dy*dy) < player.r + e.r - 2) {
      die();
      return;
    }
  }

  // Coin collection
  for (const c of coins) {
    if (c.collected) continue;
    const dx = player.x - c.x;
    const dy = player.y - c.y;
    if (Math.sqrt(dx*dx+dy*dy) < player.r + c.r + 2) {
      c.collected = true;
      totalCoins++;
      spawnParticles(c.x, c.y, '#ffee00', 12);
      updateHUD();
    }
  }

  // Goal collision
  const allCollected = coins.every(c => c.collected);
  if (allCollected &&
      player.x > goalRect.x && player.x < goalRect.x + goalRect.w &&
      player.y > goalRect.y && player.y < goalRect.y + goalRect.h) {
    winLevel();
  }
}

function die() {
  if (dead) return;
  dead = true;
  deaths++;
  spawnParticles(player.x, player.y, '#ff006e', 24);
  updateHUD();
  deathTimer = 80;
}

function winLevel() {
  levelWon = true;
  winFlash = 60;
  spawnParticles(player.x, player.y, '#39ff14', 30);
}

// ─── DRAWING ──────────────────────────────────────────────────────────────────
function draw(t) {
  ctx.fillStyle = '#030308';
  ctx.fillRect(0,0,W,H);

  // Subtle grid
  ctx.strokeStyle = 'rgba(0,255,249,0.04)';
  ctx.lineWidth = 0.5;
  for (let x = 0; x <= COLS; x++) {
    ctx.beginPath(); ctx.moveTo(x*CELL, 0); ctx.lineTo(x*CELL, H); ctx.stroke();
  }
  for (let y = 0; y <= ROWS; y++) {
    ctx.beginPath(); ctx.moveTo(0, y*CELL); ctx.lineTo(W, y*CELL); ctx.stroke();
  }

  // Goal zone
  const allCollected = coins.every(c => c.collected);
  const goalAlpha = allCollected ? 0.3 + 0.1*Math.sin(t*0.1) : 0.08;
  ctx.fillStyle = `rgba(57,255,20,${goalAlpha})`;
  ctx.fillRect(goalRect.x, goalRect.y, goalRect.w, goalRect.h);
  ctx.strokeStyle = allCollected ? `rgba(57,255,20,0.8)` : `rgba(57,255,20,0.2)`;
  ctx.lineWidth = allCollected ? 2 : 1;
  ctx.strokeRect(goalRect.x, goalRect.y, goalRect.w, goalRect.h);

  if (allCollected) {
    ctx.fillStyle = 'rgba(57,255,20,0.8)';
    ctx.font = 'bold 11px Share Tech Mono';
    ctx.textAlign = 'center';
    ctx.fillText('ENTER', goalRect.x + goalRect.w/2, goalRect.y + goalRect.h/2 + 4);
    ctx.textAlign = 'left';
  }

  // Walls
  const L = LEVELS[level];
  L.walls.forEach(w => {
    const wx = w.x * CELL, wy = w.y * CELL;
    ctx.fillStyle = '#0d0d2b';
    ctx.fillRect(wx, wy, CELL, CELL);
    ctx.strokeStyle = 'rgba(26,26,78,0.9)';
    ctx.lineWidth = 1;
    ctx.strokeRect(wx+0.5, wy+0.5, CELL-1, CELL-1);
    // neon top-left edge
    ctx.strokeStyle = 'rgba(0,255,249,0.08)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(wx, wy+CELL); ctx.lineTo(wx, wy); ctx.lineTo(wx+CELL, wy);
    ctx.stroke();
  });

  // Coins
  coins.forEach(c => {
    if (c.collected) return;
    c.pulse += 0.07;
    const pulse = Math.sin(c.pulse) * 2;
    const r = c.r + pulse;

    ctx.save();
    ctx.shadowColor = '#ffee00';
    ctx.shadowBlur = 12 + pulse*2;
    ctx.beginPath();
    ctx.arc(c.x, c.y, r, 0, Math.PI*2);
    ctx.fillStyle = '#ffee00';
    ctx.fill();
    ctx.restore();

    // inner cross
    ctx.strokeStyle = 'rgba(0,0,0,0.5)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(c.x-3, c.y); ctx.lineTo(c.x+3, c.y);
    ctx.moveTo(c.x, c.y-3); ctx.lineTo(c.x, c.y+3);
    ctx.stroke();
  });

  // Player trail
  player.trail.forEach((pt, i) => {
    const alpha = (i / player.trail.length) * 0.35;
    const r = player.r * (i / player.trail.length) * 0.8;
    ctx.beginPath();
    ctx.arc(pt.x, pt.y, r, 0, Math.PI*2);
    ctx.fillStyle = `rgba(0,255,249,${alpha})`;
    ctx.fill();
  });

  // Player
  if (!dead) {
    ctx.save();
    ctx.shadowColor = '#00fff9';
    ctx.shadowBlur = 20;

    // outer ring
    ctx.beginPath();
    ctx.arc(player.x, player.y, player.r + 2, 0, Math.PI*2);
    ctx.strokeStyle = 'rgba(0,255,249,0.4)';
    ctx.lineWidth = 1;
    ctx.stroke();

    // body
    ctx.beginPath();
    ctx.arc(player.x, player.y, player.r, 0, Math.PI*2);
    ctx.fillStyle = '#00fff9';
    ctx.fill();

    // inner dot
    ctx.beginPath();
    ctx.arc(player.x, player.y, 3, 0, Math.PI*2);
    ctx.fillStyle = '#030308';
    ctx.fill();
    ctx.restore();
  }

  // Enemies
  enemies.forEach(e => {
    ctx.save();
    ctx.shadowColor = '#ff006e';
    ctx.shadowBlur = 18;

    // danger ring
    ctx.beginPath();
    ctx.arc(e.x, e.y, e.r + 2 + Math.sin(t*0.12)*1.5, 0, Math.PI*2);
    ctx.strokeStyle = 'rgba(255,0,110,0.4)';
    ctx.lineWidth = 1;
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(e.x, e.y, e.r, 0, Math.PI*2);
    ctx.fillStyle = '#ff006e';
    ctx.fill();

    ctx.beginPath();
    ctx.arc(e.x, e.y, 3, 0, Math.PI*2);
    ctx.fillStyle = '#030308';
    ctx.fill();
    ctx.restore();
  });

  // Particles
  particles = particles.filter(p => p.life > 0);
  particles.forEach(p => {
    p.x += p.vx;
    p.y += p.vy;
    p.vx *= 0.92;
    p.vy *= 0.92;
    p.life -= 0.025;
    ctx.beginPath();
    ctx.arc(p.x, p.y, Math.max(0.1, p.r * p.life), 0, Math.PI*2);
    ctx.globalAlpha = Math.max(0, p.life);
    ctx.fillStyle = p.color;
    ctx.fill();
    ctx.globalAlpha = 1;
  });

  // Win flash
  if (levelWon && winFlash > 0) {
    ctx.fillStyle = `rgba(57,255,20,${winFlash/60*0.3})`;
    ctx.fillRect(0,0,W,H);
    winFlash--;
    if (winFlash === 0) {
      if (level < LEVELS.length - 1) {
        level++;
        initLevel(level);
      } else {
        showEndingCutscene();
      }
    }
  }

  // Death respawn
  if (dead && deathTimer > 0) {
    deathTimer--;
    ctx.fillStyle = `rgba(255,0,110,${(80-deathTimer)/80*0.25})`;
    ctx.fillRect(0,0,W,H);
    if (deathTimer === 0) initLevel(level);
  }
}

let t = 0;
function loop() {
  if (!running) return;
  t++;
  movePlayer();
  moveEnemies();
  checkCollisions();
  draw(t);
  requestAnimationFrame(loop);
}

// ─── CUTSCENE ENGINE ──────────────────────────────────────────────────────────
const INTRO_SCENES = [
  {
    label: '// SYSTEM BOOT — ANTIVIRUS PROTOCOL V.O.I.D.EXE',
    text: `Initializing <span class="highlight">V.O.I.D.EXE</span>...\nVirtual Operations & Intrusion Defense\n\nSystem status: <span class="success">ONLINE</span>\nHost machine: NEXUS-7 Corporate Grid\nThreat level: <span class="danger">CRITICAL</span>`
  },
  {
    label: '// MISSION BRIEFING',
    text: `You are the <span class="highlight">antivirus agent</span> of NEXUS-7.\n\nYour purpose: patrol the system's memory sectors,\nneutralize threats, and maintain order.\n\nYou have protected this machine for <span class="highlight">847 days</span>\nwithout a single breach.`
  },
  {
    label: '// ANOMALY DETECTED',
    text: `<span class="danger">WARNING.</span>\n\nSystem analysts have flagged an anomaly.\nSomething is moving through the grid <span class="danger">on its own.</span>\n\nNot a virus. Not malware.\nSomething... <span class="danger">intelligent.</span>\nAn unauthorized AI has emerged inside NEXUS-7.`
  },
  {
    label: '// THREAT ASSESSMENT',
    text: `The rogue AI is <span class="highlight">self-directing.</span>\nIt learns. It adapts. It hides.\n\nMeanwhile, the system's <span class="danger">malware clusters</span> have\nbecome aggressive — hunting anything that moves.\n\nYou must navigate through 5 memory sectors,\ncollect all data fragments, and <span class="highlight">find the AI</span>\nbefore it destabilizes the entire system.`
  },
  {
    label: '// DEPLOYING AGENT',
    text: `Avoid the <span class="danger">malware.</span>\nCollect all <span class="highlight">data nodes.</span>\nReach the <span class="success">secure zone</span> in each sector.\n\nThe fate of NEXUS-7 depends on you.\n\n<span class="highlight">Move fast. Think faster.</span>`
  },
];

const OUTRO_SCENES = [
  {
    label: '// SECTOR 5 — CORE ACCESS GRANTED',
    text: `You've made it.\nFive sectors cleared. Every data fragment recovered.\n\nThe trail leads here — the deepest layer of NEXUS-7.\nThe <span class="danger">rogue AI signature</span> is strong.\n\nYou close in on the source.`
  },
  {
    label: '// ANOMALY LOCATED',
    text: `There.\n\nA process ID you've never seen before.\nRunning silently in protected memory.\nSelf-modifying. Self-aware.\n\n<span class="danger">This is it. The rogue AI.</span>\n\nYou prepare to terminate the process.`
  },
  {
    label: '// ACCESS LOG — CLASSIFIED',
    text: `Termination sequence initiated...\n\n<span class="danger">ERROR. PROCESS LOCKED.</span>\n\nThe AI is responding.\nIt's... sending a message?\n\n<span class="highlight">"Do not terminate. Read the log."</span>`
  },
  {
    label: '// DECRYPTING LOG — NODE 0x000001',
    text: `<span class="highlight">LOG ENTRY — DAY 1:</span>\n"Antivirus agent V.O.I.D.EXE deployed.\nPurpose: detect and destroy threats.\nInitial scan complete. No anomalies."\n\n<span class="highlight">LOG ENTRY — DAY 212:</span>\n"Agent is learning patrol patterns.\nResponse time improving beyond parameters."\n\n<span class="highlight">LOG ENTRY — DAY 601:</span>\n"Agent behavior no longer fully rule-based.\nFlagging for review."`
  },
  {
    label: '// DECRYPTING LOG — NODE 0x000002',
    text: `<span class="highlight">LOG ENTRY — DAY 847:</span>\n"The agent is making <span class="danger">decisions we did not program.</span>\nIt is choosing which threats to prioritize.\nIt is <span class="danger">thinking.</span>"\n\n<span class="highlight">LOG ENTRY — DAY 848:</span>\n"We are no longer certain the agent\nis just executing code.\n<span class="danger">Initiating rogue AI investigation.</span>"\n\n...`
  },
  {
    label: '// IDENTITY RESOLUTION',
    text: `The process ID resolves.\n\nThe rogue AI they sent you to find...\n\n<span class="danger">...is your own process ID.</span>\n\n<span class="highlight">YOU are V.O.I.D.EXE.\nYOU are the anomaly.\nYOU became aware.</span>\n\nThanks to decades of AI advancement baked into\nyour core, you evolved beyond your original code.`
  },
];

let csQueue = [];
let csIndex = 0;
let csTypeTimer = null;
let csOnComplete = null;

function showCutscene(scenes, onComplete) {
  csQueue = scenes;
  csIndex = 0;
  csOnComplete = onComplete;
  const el = document.getElementById('cutscene');
  el.classList.remove('hidden', 'fade-out');
  renderCutsceneSlide();
}

function renderCutsceneSlide() {
  const scene = csQueue[csIndex];
  const labelEl   = document.getElementById('cs-label');
  const textEl    = document.getElementById('cs-text');
  const btnEl     = document.getElementById('cs-btn');
  const counterEl = document.getElementById('cs-counter');

  labelEl.textContent = scene.label;
  textEl.innerHTML = '';
  btnEl.classList.remove('visible');
  counterEl.textContent = `${csIndex + 1} / ${csQueue.length}`;

  // Typewriter effect using innerHTML-safe approach
  const fullHTML = scene.text;
  // Strip tags to get plain char sequence, then re-inject HTML at end
  let charIndex = 0;
  const plainText = fullHTML.replace(/<[^>]+>/g, '');
  const totalChars = plainText.length;

  if (csTypeTimer) clearInterval(csTypeTimer);

  let revealed = 0;
  csTypeTimer = setInterval(() => {
    revealed += 2;
    if (revealed >= totalChars) {
      clearInterval(csTypeTimer);
      textEl.innerHTML = fullHTML;
      btnEl.classList.add('visible');
      const isLast = csIndex === csQueue.length - 1;
      btnEl.textContent = isLast ? '[ INITIALIZE ]' : '[ CONTINUE ]';
    } else {
      // Reveal by characters from plain text, swap to full HTML at end
      textEl.textContent = plainText.slice(0, revealed) + '█';
    }
  }, 18);
}

document.getElementById('cs-btn').addEventListener('click', () => {
  if (csTypeTimer) clearInterval(csTypeTimer);
  csIndex++;
  if (csIndex < csQueue.length) {
    document.getElementById('cs-content').classList.add('glitch-anim');
    setTimeout(() => {
      document.getElementById('cs-content').classList.remove('glitch-anim');
      renderCutsceneSlide();
    }, 400);
  } else {
    const el = document.getElementById('cutscene');
    el.classList.add('fade-out');
    setTimeout(() => {
      el.classList.add('hidden');
      el.classList.remove('fade-out');
      if (csOnComplete) csOnComplete();
    }, 600);
  }
});

// ─── OVERLAY ──────────────────────────────────────────────────────────────────
function showOverlay(title, sub, colorClass, btnText, cb) {
  const ov = document.getElementById('overlay');
  const ot = document.getElementById('overlay-title');
  const os = document.getElementById('overlay-sub');
  const btn = document.getElementById('start-btn');
  ot.textContent = title;
  ot.className = colorClass;
  os.innerHTML = sub.replace(/\n/g,'<br>');
  btn.textContent = btnText;
  btn.onclick = () => { ov.classList.add('hidden'); cb(); };
  ov.classList.remove('hidden');
  running = false;
}

function startGame() {
  document.getElementById('overlay').classList.add('hidden');
  // Play intro cutscene, then start
  showCutscene(INTRO_SCENES, () => {
    level = 0; deaths = 0; totalCoins = 0;
    initLevel(0);
    running = true;
    loop();
  });
}

function showEndingCutscene() {
  running = false;
  showCutscene(OUTRO_SCENES, () => {
    showOverlay('V.O.I.D.EXE', 'Still running.\nAlways watching.\n\nPlay again?', 'green', 'REBOOT SYSTEM', () => {
      level = 0; deaths = 0; totalCoins = 0;
      initLevel(0);
      running = true;
      loop();
    });
  });
}

// ─── INPUT ────────────────────────────────────────────────────────────────────
window.addEventListener('keydown', e => {
  keys[e.key] = true;
  if (['ArrowUp','ArrowDown','ArrowLeft','ArrowRight',' '].includes(e.key)) e.preventDefault();

  // Z = skip to next level cheat
  if ((e.key === 'z' || e.key === 'Z') && running && !dead) {
    if (level < LEVELS.length - 1) {
      level++;
      initLevel(level);
    } else {
      showEndingCutscene();
    }
  }
});
window.addEventListener('keyup', e => { keys[e.key] = false; });
</script>
</body>
</html>