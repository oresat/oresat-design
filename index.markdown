---
title: OreSat 0 Design Requirements
---

# Meeting Notes

## 2015

<ul>
{% for note in site.posts %}
    {% assign d = note.date | date: "%-d"  %}
    <li><a href=".{{ note.url }}">{{ note.date | date: "%B" }}
    {% case d %}
        {% when '1' or '21' or '31' %}{{ d }}<sup>st</sup>
        {% when '2' or '22' %}{{ d }}<sup>nd</sup>
        {% when '3' or '23' %}{{ d }}<sup>rd</sup>
        {% else %}{{ d }}<sup>th</sup>
    {% endcase %}</a></li>
{% endfor %}
</ul>
