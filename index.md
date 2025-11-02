---
layout: default
title: "PyTorch Transformer Notes"
description: "Learning notes about PyTorch and Transformers"
---

# PyTorch Transformer Notes

Welcome to my learning notes about PyTorch and Transformer architectures.

## Recent Notes
{% for post in site.posts limit:5 %}
- [{{ post.title }}]({{ site.baseurl }}{{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}

## Wiki Pages
{% assign wiki_pages = site.pages | where_exp: "item", "item.path contains 'wiki/'" %}
{% for page in wiki_pages %}
- [{{ page.title }}]({{ site.baseurl }}{{ page.url }})
{% endfor %}