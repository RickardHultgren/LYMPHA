function changeMenu() {
	if (document.getElementById("menuish").style.display == 'block') {
		document.getElementById("menuish").style.display = 'none'
	} else {
		document.getElementById("menuish").style.display = 'block'
	}
}

document.write("<font style=\"font-family: \"Merriweather\",\"Droid Serif\", Georgia, 'Times New Roman', Times, serif;\"><div class=\"container\" style=\"\"");
document.write("	<div id=\"menubig\" style=\"overflow:hidden;font-size:1.5vw; text-align:center; \" id=\"thetop\">");
document.write("		<div style=\"font-size:1.5vw;margin:0vw 20vw 0vw 20vw ;width:60vw; ;float:left; margin-bottom:0.5em;border-bottom:0.1em solid #cccccc;\"><a href=\"index.html\"><img id=\"logopic\" src=\"logo.png\">");
document.write("		<\/a><span style=\"float:right;display:block;padding:2.5em 1.5em 0.5em  0.5em;font-size:0.99em;letter-spacing:0em;color:#6400EF;font-weight:bold;\">BUILDING VALUE IN MEDICAL REASONING<\/span>");
document.write("	<div style=\"border-top:0.2vw solid #cccccc;text-align:center;z-index:3;\">");
document.write("		<a id=\"indextext\" href=\"index.html\"><div class=\"menu2\" id=\"index\">HOME<\/div><\/a> ");
document.write("		<a id=\"docstext\" href=\"docs.html\"><div class=\"menu2\" id=\"docs\">DOCS<\/div><\/a>");
document.write("		<a id=\"downloadstext\" href=\"downloads.html\"><div class=\"menu2\" id=\"downloads\">DOWNLOADS<\/div><\/a>");
document.write("		<a id=\"blogtext\" href=\"http://lymphascripting.blogspot.se/\"><div class=\"menu2\" id=\"blog\">BLOG<\/div><\/a>");
//document.write("		<a id=\"contacttext\" href=\"contact.html\"><div class=\"menu2\" id=\"contact\">CONTACT<\/div><\/a>");
//document.write("		<a id=\"historytext\" href=\"history.html\"><div class=\"menu2\" id=\"history\">HISTORY<\/div><\/a>");
document.write("	<\/div>");
document.write("<\/div><\/div> ");
document.write("<div id=\"menusmall\" style=\"text-align:center;\">");
document.write("	<a style=\"vertical-align:top;\" href=\"index.html\"><img src=\"logo.png\" alt=\"LYMPHA\" style=\"height:auto;width:60vw;margin-right:4em;vertical-align:bottom;\" ;\"><\/a>");
document.write("	<div style=\"width:4em;height:4em;position:absolute;\"> <\/div><div class=\"menubutton\" style=\"font-style:normal;vertical-align:top;color:#EFAB00;margin-bottom:-0em;font-size:20vw;border:none;display:inline-block;position: absolute;right:-.25em;top:-.38em;\" onclick=\"changeMenu();\">&#8801;<\/div><BR>");
document.write("	<div id=\"menuish\" style=\"width=100%;display:none;position:relative;z-index:1;\">");
document.write("		<a href=\"index.html\"><div id=\"indexsmall\" class=\"menu2\">HOME<\/div><\/a>");
document.write("		<a href=\"docs.html\"><div id=\"docssmall\" class=\"menu2\">DOCS<\/div><\/a>");
document.write("		<a href=\"downloads.html\"><div id=\"downloadssmall\" class=\"menu2\">DOWNLOADS<\/div><\/a>");
document.write("		<a id=\"blogsmall\" href=\"http://lymphascripting.blogspot.se/\"><div class=\"menu2\" id=\"blog\">BLOG<\/div><\/a>");
//document.write("		<a href=\"history.html\"><div id=\"historysmall\" class=\"menu2\">HISTORY<\/div><\/a>");
//document.write("		<a href=\"contact.html\"><div id=\"contactsmall\" class=\"menu2\">CONTACT<\/div><\/a>");
document.write("	<\/div>");
document.write("<hr style=\"z-index:1;position:relative;\"><\/div>");
