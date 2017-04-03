<script>
document.getElementById("blogsmall").style.backgroundColor="#EFAB00";
document.getElementById("blogtext").style.color="#000000";
document.getElementById("blog").className="menu2active";
</script>

{% for post in site.posts %}
{{ post.date | date_to_string }} &raquo; <a href="/lympha{{post.url}}">{{ post.title }}</a>/lympha{{post.url}}
{% endfor %}

