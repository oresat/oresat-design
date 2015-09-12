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

<div markdown="1" style="font-size:0.9em;margin-top:100px;color:#999;" id="newnote">
[+ New meeting note](https://github.com/oresat/oresat-design/new/gh-pages/_posts?filename=YYYY-MM-DD-notes.markdown)
</div>
<script>
    var now = new Date();
    var year = now.getFullYear();
    var month = now.getMonth();
    if (month < 10) month = "0"+month;
    var day = now.getDay();
    if (day < 10) day = "0"+day;
    var meetingnote = year + "-" + month + "-" + day + "-notes.markdown"
    document.getElementById('newnote').children[0].children[0].href = "https://github.com/oresat/oresat-design/new/gh-pages/_posts?filename="+meetingnote;
</script>
