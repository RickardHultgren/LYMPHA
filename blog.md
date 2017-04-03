<script>
document.getElementById("blogsmall").style.backgroundColor="#EFAB00";
document.getElementById("blogtext").style.color="#000000";
document.getElementById("blog").className="menu2active";
</script>
<br><br>
[<span style="background-color:#444444;color:#FFFFFF;width:auto;height:1em;text-align:center;position:relative;"><span style="font-size:2em;">.</span><span style="font-size:0.5em;">&#41;</span><span style="font-size:1em;">&#41;</span></span> atom feed](http://rickardhultgren.github.io/lympha/atom.xml)
<br><br>
{% for post in site.posts %}
{{ post.date | date_to_string }} &raquo; <a href="/lympha{{post.url}}">{{ post.title }}</a>
{% endfor %}

