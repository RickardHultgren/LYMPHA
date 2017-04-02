	<script>
	document.getElementById("indexsmall").style.backgroundColor="#EFAB00";
	document.getElementById("indextext").style.color="#000000";
	document.getElementById("index").className="menu2active";
	</script>
  <ul class="posts">
      {% for post in site.posts %}
        <li><span class="date">{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
