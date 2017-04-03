<script>
document.getElementById("blogsmall").style.backgroundColor="#EFAB00";
document.getElementById("blogtext").style.color="#000000";
document.getElementById("blog").className="menu2active";
</script>
<br><br>
[<i class="material-icons" style="background-color:#998855;color:#ffffff;">rss_feed</i> atom feed](http://rickardhultgren.github.io/lympha/atom.xml)
<br><br>
{% for post in site.posts %}
{{ post.date | date_to_string }} &raquo; <a href="/lympha{{post.url}}">{{ post.title }}</a>
{% endfor %}

