---
layout: default
---
<script>
document.getElementById( "blogsmall").style.backgroundColor="#EFAB00";
document.getElementById( "blogtext").style.color="#000000";
document.getElementById( "blog").className="menu2active";
</script>
<p class="container">
<p>
{% for post in site.posts %}
* <span class="date">{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a>
{% endfor %}
</p>
</p>
