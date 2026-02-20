---
layout: page 
title: About
permalink: /about/
---

### As a conversation Starter

I like hanging out with friends, watching cricket or basketball, and generally relaxing.

I also love trivia

BIG Cricket fan - I'm the #1 Dhoni Supporter

I've been to over 23 countries and 5 continents (including Antarctica), here are my favorites below:

<style>
    /* Style looks pretty compact, 
       - grid-container and grid-item are referenced the code 
    */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Dynamic columns */
        gap: 10px;
    }
    .grid-item {
        text-align: center;
    }
    .grid-item img {
        width: 100%;
        height: 100px; /* Fixed height for uniformity */
        object-fit: contain; /* Ensure the image fits within the fixed height */
    }
    .grid-item p {
        margin: 5px 0; /* Add some margin for spacing */
    }

    .image-gallery {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        gap: 10px;
        }

    .image-gallery img {
        max-height: 150px;
        object-fit: cover;
        border-radius: 5px;
    }
</style>

<!-- This grid_container class is used by CSS styling and the id is used by JavaScript connection -->
<div class="grid-container" id="grid_container">
    <!-- content will be added here by JavaScript -->
</div>

<script>
    // 1. Make a connection to the HTML container defined in the HTML div
    var container = document.getElementById("grid_container"); // This container connects to the HTML div

    // 2. Define a JavaScript object for our http source and our data rows for the Living in the World grid
    var http_source = "https://flagcdn.com/";
    var living_in_the_world = [
        {"flag": "us-ca.svg", "greeting": "Hi", "description": "California - Lived here my whole life, born in San Diego"},
        {"flag": "in.svg", "greeting": "Namaste", "description": "India - Country of origin, my parents and family all come from there"},
        {"flag": "gr.svg", "greeting": "Yasou", "description": "Greece - I visited and loved it, I also love reading about its myths and stories"},
        {"flag": "us-hi.svg", "greeting": "Aloha", "description": "Hawaii - visited and loved it! Great surfing, especially on Oahu"},
    ];

    // 3a. Consider how to update style count for size of container
    // The grid-template-columns has been defined as dynamic with auto-fill and minmax

    // 3b. Build grid items inside of our container for each row of data
    for (const location of living_in_the_world) {
        // Create a "div" with "class grid-item" for each row
        var gridItem = document.createElement("div");
        gridItem.className = "grid-item";  // This class name connects the gridItem to the CSS style elements
        // Add "img" HTML tag for the flag
        var img = document.createElement("img");
        img.src = http_source + location.flag; // concatenate the source and flag
        img.alt = location.flag + " Flag"; // add alt text for accessibility

        // Add "p" HTML tag for the description
        var description = document.createElement("p");
        description.textContent = location.description; // extract the description

        // Add "p" HTML tag for the greeting
        var greeting = document.createElement("p");
        greeting.textContent = location.greeting;  // extract the greeting

        // Append img and p HTML tags to the grid item DIV
        gridItem.appendChild(img);
        gridItem.appendChild(description);
        gridItem.appendChild(greeting);

        // Append the grid item DIV to the container DIV
        container.appendChild(gridItem);
    }
</script>

<!-- Favorite TV Shows grid -->
## Favorite TV Shows

<style>
    /* Favorite shows card layout */
    .shows-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 18px;
        align-items: start;
    }
    .show-card {
        background: #2b2b2b;
        color: #eee;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 6px rgba(0,0,0,0.4);
        display: flex;
        flex-direction: column;
        border: 3px solid transparent; /* colored per-card */
        min-width: 0;
    }
    .show-header {
        padding: 10px 12px;
        font-weight: 700;
        text-align: center;
        background: rgba(255,255,255,0.03);
        border-bottom: 1px solid rgba(255,255,255,0.04);
    }
    .show-body {
        padding: 12px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        align-items: center;
    }
    .show-body img {
        width: 160px;
        height: 160px;
        object-fit: cover;
        border-radius: 6px;
        background: #111;
    }
    .show-desc {
        font-size: 0.95rem;
        color: #d6d6d6;
        text-align: center;
    }

    /* Responsive */
    @media (max-width: 900px) {
        .shows-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }
    @media (max-width: 520px) {
        .shows-grid { grid-template-columns: 1fr; }
        .show-card { width: 90%; max-width: 420px; margin: 0 auto; }
    }
</style>

<div class="shows-grid" id="shows_grid">
    <!-- Favorite shows will be rendered here -->
</div>

<script>
    // Base path for local images (place your images in /images/fav_shows/)
    var site_base = "{{ site.baseurl | default: '' }}";
    var shows_http_source = (site_base && site_base !== '')
        ? (site_base.replace(/\/$/, '') + '/images/fav_shows/')
        : '{{ site.baseurl }}/images/fav_shows/';

    var favorite_shows = [
        {"img": "Sakamoto_Days.webp", "title": "Sakamoto Days", "desc": "A goofy, action-packed series I love for its humor and heart"},
        {"img": "Bleach.webp", "title": "Bleach — TYBW", "desc": "Epic supernatural battles and memorable characters"},
        {"img": "White_Collar.jpeg", "title": "White Collar", "desc": "Smart, stylish crime-procedural with great chemistry"},
        {"img": "Sienfeld.webp", "title": "Seinfeld", "desc": "Classic sitcom about nothing — endlessly rewatchable with family!"}
    ];

    var colors = ['#2ecc71', '#5DADE2', '#8e44ad', '#ff6eb4'];

    var showsContainer = document.getElementById("shows_grid");
    favorite_shows.forEach(function(show, idx) {
        var card = document.createElement('div');
        card.className = 'show-card';
        card.style.borderColor = colors[idx % colors.length];

        var header = document.createElement('div');
        header.className = 'show-header';
        header.textContent = show.title;

        var body = document.createElement('div');
        body.className = 'show-body';

        var img = document.createElement('img');
        img.src = shows_http_source + encodeURIComponent(show.img);
        img.alt = show.title;

        var desc = document.createElement('div');
        desc.className = 'show-desc';
        desc.textContent = show.desc;

        body.appendChild(img);
        body.appendChild(desc);

        card.appendChild(header);
        card.appendChild(body);

        showsContainer.appendChild(card);
    });
</script>

<!-- Favorite Video Games (cards like shows) -->
## Favorite Video Games

<div class="shows-grid" id="games_grid">
    <!-- Game cards will be rendered here -->
    </div>

<script>
        // Use local images stored under /images/games/ and update descriptions
        var games_http_source = (site_base && site_base !== '')
            ? (site_base.replace(/\/$/, '') + '/images/games/')
            : '{{ site.baseurl }}/images/games/';

        var games = [
            {"img": "minecraft.png", "title": "Minecraft", "desc": "I love exploring new worlds, trying out challenging mods (Yes, I beat RLCraft), and playing with friends"},
            {"img": "genshin.svg", "title": "Genshin Impact", "desc": "I love the open-world exploring and partying up with friends, though sometimes the grind gets a little boring"},
            {"img": "fire-emblem-blazing-blade.jpg", "title": "Fire Emblem", "desc": "I love the GBA games especially, and my favorite is the Blazing Blade. Hector just has that aura"},
            {"img": "pokemon-emerald.jpg", "title": "Pokémon", "desc": "I love most Pokemon, though the new ones have fallen off. Charizard and Grookey are my favorites"}
        ];

        var gamesContainer = document.getElementById('games_grid');
        var gameColors = ['#3cb371', '#d07ef0', '#ff7f50', '#ffd700'];

        games.forEach(function(game, idx) {
            var card = document.createElement('div');
            card.className = 'show-card';
            card.style.borderColor = gameColors[idx % gameColors.length];

            var header = document.createElement('div');
            header.className = 'show-header';
            header.textContent = game.title;

            var body = document.createElement('div');
            body.className = 'show-body';

            var img = document.createElement('img');
            img.src = games_http_source + encodeURIComponent(game.img);
            img.alt = game.title;

            var desc = document.createElement('div');
            desc.className = 'show-desc';
            desc.textContent = game.desc;

            body.appendChild(img);
            body.appendChild(desc);

            card.appendChild(header);
            card.appendChild(body);

            gamesContainer.appendChild(card);
        });
    </script>

### Journey through Life

- 🏫 Up to high school at Del Norte in California
- 🏫 High school not yet over, lets go year of '28
- Traveled to over 23 countries!
- Scouting America!
- DECA
- Quizbowl & A-League are peak 
- I play a LOT of games:
- Hollow Knight - both
- Started League
- Pokemon
- Fire Emblem
- Anime is good: 
- Sakamoto Days
- Wind Breaker
- SAO
- Bleach

### About Me

For me, everything is my family and friends

- I speak English, Tamil, and un poco de Espanol
- Love to explore the great outdoors, camping, hiking, backpacking
- Slept in a hammock overnight several times
- Gamer
- Love to be involved in the community
- Gotta love food of course
- Gonna be a businessman or lawyer or smth, not sure - just not STEM
- "Don't break anyone's heart, they only have one. Break their bones instead, they have 206". - Ichigo K.
- "Shoot for the moon, because if you miss, you'll land amongst the stars". - I forgot who said this

<comment>
My most aura pics 🔥 Go to my main page to see a goated edit of me in full aura mode
</comment>
<div class="image-gallery">
    <img src="{{ site.baseurl }}/images/about/Shotgun.png" alt="Image 1">
    <img src="{{ site.baseurl }}/images/about/NYLT.png" alt="Image 2">
    <img src="{{ site.baseurl }}/images/about/Tuff.jpeg" alt="Image 3">
</div>
