---
layout: single
title: Birds & Insects
permalink: /gallery/birds/
---

Bird and insect paintings from the garden and countryside.

<div class="painting-grid">

{% assign paintings = site.paintings | where:"category","birds" %}

{% for painting in paintings %}

{% assign thumb = painting.image | replace: ".jpg", "-thumb.jpg" %}

<a class="painting-card" href="{{ painting.url }}">

  <img src="/assets/images/paintings/thumbs/{{ thumb }}"
       alt="{{ painting.title }}">

  <h3>{{ painting.title }}</h3>

  {% if painting.year %}
  <p class="painting-year">{{ painting.year }}</p>
  {% endif %}

</a>

{% endfor %}

</div>