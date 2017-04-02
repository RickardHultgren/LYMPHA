---
layout: default
---
<script>
document.getElementById( "blogsmall").style.backgroundColor="#EFAB00";
document.getElementById( "blogtext").style.color="#000000";
document.getElementById( "blog").className="menu2active";
</script>
    <ul class="posts">
      {% for post in site.posts %}
        <li><span class="date">{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
