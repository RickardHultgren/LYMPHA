<script>
document.getElementById("blogsmall").style.backgroundColor="#EFAB00";
document.getElementById("blogtext").style.color="#000000";
document.getElementById("blog").className="menu2active";
</script>
<br><br>
[<i class="material-icons" style="background-color:#EFAB00;color:#ffffff;font-size:1.5em;margin-top:.5em; margin-bottom:-.5em;display: inline-block; position: static;vertical-align: top;">rss_feed</i><span style="vertical-align: middle;"> atom feed </span> ](http://rickardhultgren.github.io/lympha/atom.xml)
<br><br>
{% for post in site.posts %}
{{ post.date | date_to_string }} &raquo; <a href="/lympha{{post.url}}">{{ post.title }}</a>
{% endfor %}

