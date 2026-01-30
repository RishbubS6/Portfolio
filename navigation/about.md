---
layout: page 
title: About
permalink: /about/
---

## As a conversation Starter

I like random occurences and relaxing.

Love trivia - will digest random facts like a maniac

BIG Cricket fan - I'm the #1 Dhoni Supporter

I've been to over 23 countries and 5 continents (including Antarctca), here are my favorites below:

<comment>
Flags from Wikipedia Images
</comment>

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
        {"flag": "us-ca.svg", "greeting": "Hi", "description": "California - My whole life"},
        {"flag": "in.svg", "greeting": "Namaste", "description": "India - Country of origin"},
        {"flag": "gr.svg", "greeting": "Yasou", "description": "Greece - visited"},
        {"flag": "us-hi.svg", "greeting": "Aloha", "description": "Hawaii - visited and loved it"},
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

<div class="grid-container" id="shows_grid">
    <!-- Favorite shows will be added here by JavaScript -->
</div>

<script>
    // Base path for local images (place your images in /images/fav_shows/)
    var site_base = "{{ site.baseurl | default: '' }}";
    var shows_http_source = (site_base && site_base !== '')
        ? (site_base.replace(/\/$/, '') + '/images/fav_shows/')
        : './images/fav_shows/';
    var favorite_shows = [
        {"img": "Sakamoto_Days.webp", "title": "Sakamoto Days"},
        {"img": "Bleach.webp", "title": "Bleach — TYBW"},
        {"img": "White_Collar.jpeg", "title": "White Collar"},
        {"img": "Sienfeld.webp", "title": "Seinfeld"}
    ];

    var showsContainer = document.getElementById("shows_grid");
    for (const show of favorite_shows) {
        var item = document.createElement("div");
        item.className = "grid-item";
        var img = document.createElement("img");
        img.src = shows_http_source + encodeURIComponent(show.img);
        img.alt = show.title;
        var p = document.createElement("p");
        p.textContent = show.title;
        item.appendChild(img);
        item.appendChild(p);
        showsContainer.appendChild(item);
    }
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

- Soy Indiano
- I speak English, Tamil, and un poco de Espanol
- Love to go to the great outdoors, camping, hiking, backpacking
- Slept in a hammock overnight several times
- Gamer
- Love to be involved in the community
- Gotta love food ofc
- Gonna be a businessman or lawyer or smth, not sure - just not STEM
- "Don't break anyone's heart, they only have one. Break their bones instead, they have 206". - Ichigo K.
- "Shoot for the moon, because if you miss, you'll land amongst the stars". - I forgot who said this

<comment>
My most aura pics 🔥Go to my main page to see a goated edit of me in full aura mode
</comment>
<div class="image-gallery">
    <img src="{{ site.baseurl }}/images/about/Shotgun.png" alt="Image 1">
    <img src="{{ site.baseurl }}/images/about/NYLT.png" alt="Image 2">
    <img src="{{ site.baseurl }}/images/about/Tuff.jpeg" alt="Image 3">
</div>
