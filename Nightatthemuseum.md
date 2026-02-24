---
layout: post
codemirror: true
microblog: true
title: Night at the Museum Learning Blog
permalink: /nightatthemuseum
author: Rishab Shyamal
---

*** Night at the Museum ***
At N@TM I saw all of the computer science classes (CSSE, AP CSP, and AP CSA) showcase their major achievements this trimester and talk about how they worked. A lot of the AP CSP projects were advanced games or interactive courses (For example, I noticed Aniska's group had made a course teaching ), and I noticed that AP CSA's projects all seemed related to what we do in CSSE. (For example, I saw Xavier's group had helped to develop the gamebuilder we used for our RPG game, which I thought was really cool)

*** Presenting our class game ***
At N@TM our class presented our RPG game (at least the parts that worked) to everyone who came by to our table. I presented on the TV in the back and we let everyone try out our game and then explained some of the work that went into it, includng sprites, code, and npcs. We also created a feedback form, and the general consensus for our feedback was that the game mechanics could be improved to make it more in depth, which we had expected.

*** Gallery of Images from N@TM ***
<style>
.natm-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(180px,1fr));
  gap: 10px;
  margin: 1rem 0;
}
.natm-item{ position:relative; overflow:hidden; border-radius:8px; display:block; text-decoration:none; color:inherit;}
.natm-item img{ width:100%; height:100%; object-fit:cover; transition:transform .35s ease, filter .35s ease; display:block;}
.natm-item:hover img{ transform:scale(1.08); filter:brightness(.9) saturate(1.05);}
.natm-caption{ position:absolute; bottom:6px; left:6px; right:6px; color:#fff; font-size:0.85rem; text-shadow:0 2px 6px rgba(0,0,0,.6); background:linear-gradient(transparent, rgba(0,0,0,.25)); padding:6px; border-radius:6px;}
.lightbox{ display:none; position:fixed; inset:0; background:rgba(0,0,0,.85); align-items:center; justify-content:center; z-index:1000; padding:2vh;}
.lightbox img{ max-width:95%; max-height:92%; box-shadow:0 10px 40px rgba(0,0,0,.6); border-radius:6px;}
.lightbox:target{ display:flex;}
</style>

{% assign gallery_images = site.static_files | where_exp: "f", "f.path contains '/images/N@TMBlog/'" | sort: "name" %}
<div class="natm-gallery">
{% for img in gallery_images %}
  <a class="natm-item" href="#lightbox-{{ forloop.index }}">
    <img src="{{ img.path | relative_url | replace: ' ', '%20' | replace: '(', '%28' | replace: ')', '%29' | replace: '#', '%23' | replace: '&', '%26' }}" alt="{{ img.name }}">
    <div class="natm-caption">{{ img.name | split:'.' | first | replace: '-', ' ' | replace: '_', ' ' }}</div>
  </a>

  <div id="lightbox-{{ forloop.index }}" class="lightbox">
    <a href="#" style="position:absolute;inset:0;"></a>
    <img src="{{ img.path | relative_url | replace: ' ', '%20' | replace: '(', '%28' | replace: ')', '%29' | replace: '#', '%23' | replace: '&', '%26' }}" alt="{{ img.name }}">
  </div>
{% endfor %}
</div>

