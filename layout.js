function changeMenu() {
	if (document.getElementById("menuish").style.display == 'block') {
		document.getElementById("menuish").style.display = 'none'
	} else {
		document.getElementById("menuish").style.display = 'block'
	}
}

document.write("<font style=\"font-family: \"Merriweather\",\"Droid Serif\", Georgia, 'Times New Roman', Times, serif;\"><div class=\"container\" ");
document.write("	<div id=\"menubig\" style=\"overflow:hidden;margin: 0px auto 0px auto; text-align:center; border:0em;border-bottom:2px; border-style:solid; border-color:#777777;\" id=\"thetop\">");
document.write("		<div style=\"float:left;width:auto;width:95%;padding:1em 0px 1em 0px;height:7em;background-size:cover;background-size:150px, auto;background-repeat:no-repeat;margin:0.2em 0px 2px 0px;width:15%; height:auto;\"><a href=\"index.html\" style=\'font-family:\"Share Tech Mono\",\"Lucida Console\",Monospace,\"DejaVu Sans Mono\",\"Courier New\",MiscFixed; font-size:9px;\'><img id=\"logopic\" src=\"logo.png\" style=\"margin:1.8em 0em 0em 0em; float:left;\"><br>");
document.write("		</a><\/div><br><br><span class=\"subtitle\" style=\"font-size:18px;color:#6400EF;margin-left:-2.5em;\">THE LANGUAGE FOR MEDICAL ALGORITHMS</span><br>");
document.write("		<a id=\"contacttext\" href=\"contact.html\"><div class=\"menu2\" id=\"contact\">CONTACT<\/div><\/a>");
document.write("		<a id=\"historytext\" href=\"history.html\"><div class=\"menu2\" id=\"history\">HISTORY<\/div><\/a>");
document.write("		<a id=\"blogtext\" href=\"http://lymphascripting.blogspot.se/\"><div class=\"menu2\" id=\"blog\">BLOG<\/div><\/a>");
document.write("		<a id=\"downloadstext\" href=\"downloads.html\"><div class=\"menu2\" id=\"downloads\">DOWNLOADS<\/div><\/a>");
document.write("		<a id=\"docstext\" href=\"docs.html\"><div class=\"menu2\" id=\"docs\">DOCS<\/div><\/a>");
document.write("		<a id=\"indextext\" href=\"index.html\"><div class=\"menu2\" id=\"index\">HOME<\/div><\/a>");
document.write("	<\/div> ");
document.write("<\/div> ");
document.write("<div id=\"menusmall\" style=\"text-align:center;border-style: solid;border-bottom: thick solid #aaaaaa;\">");
document.write("	<img id=\"menubutton\" src=\"logo.png\" alt=\"LYMPHA\" style=\"height:auto;width:50%;max-width:250px;\" onclick=\"changeMenu();\">");
document.write("	<img id=\"menubutton\" src=\"menu.png\" alt=\"MENU\" style=\"height:auto;width:25%;max-width:84px;\" onclick=\"changeMenu();\">");
document.write("	<div id=\"menuish\" style=\"width=100%;display:none;\">");
document.write("		<a href=\"index.html\"><div id=\"indexsmall\" class=\"menu2\">HOME<\/div><\/a>");
document.write("		<a href=\"docs.html\"><div id=\"docssmall\" class=\"menu2\">DOCS<\/div><\/a>");
document.write("		<a id=\"downloadssmall\" href=\"https://sourceforge.net/projects/lymphascripting/files/?\"><div class=\"menu2\" id=\"downloads\">DOWNLOADS<\/div><\/a>");
document.write("		<a id=\"blogsmall\" href=\"http://lymphascripting.blogspot.se/\"><div class=\"menu2\" id=\"blog\">BLOG<\/div><\/a>");
document.write("		<a href=\"history.html\"><div id=\"historysmall\" class=\"menu2\">HISTORY<\/div><\/a>");
document.write("		<a href=\"contact.html\"><div id=\"contactsmall\" class=\"menu2\">CONTACT<\/div><\/a>");
document.write("	<\/div>");
document.write("<\/div>");
