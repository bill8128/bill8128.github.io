---
layout: single
title: Gallery
permalink: /gallery/
---

<div class="painting-grid">

{% assign sorted_paintings = site.paintings | sort: "date_added" | reverse %}

{% for painting in sorted_paintings %}

{% assign filename = painting.image | replace: ".jpg", "" %}
{% assign thumbname = filename | append: "-thumb.jpg" %}

<div class="painting-card">

<a href="{{ painting.url }}">

<img src="/assets/images/paintings/thumbs/{{ thumbname }}"
     alt="{{ painting.title }}">

</a>

<h3>{{ painting.title }}</h3>

</div>

{% endfor %}

</div>