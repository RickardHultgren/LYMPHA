<script>
document.getElementById("indexsmall").style.backgroundColor="#EFAB00";
document.getElementById("indextext").style.color="#000000";
document.getElementById("index").className="menu2active";
</script>

{% for post in site.posts %}
{{ post.date | date_to_string }} &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}

