<script>
document.getElementById( "aboutsmall").style.backgroundColor="#EFAB00";
document.getElementById( "abouttext").style.color="#000000";
document.getElementById( "about").className="menu2active";
</script>
<span class="sc">Lympha</span> is a logical language for formulating and handling medical algorithms. The aim of the project is to provide syntax guidelines as well as structural rules for reading <span class="sc">lympha</span> scripts. Interpreters and compilers are built upon those rules. The <span class="sc">lympha</span> project is open-source, licensed under the <span class="sc">[bsd 2](http://opensource.org/licenses/BSD-2-Clause)</span> license.<br><br>
<br>
<a name="progress" style="font-weight:bold;"></a>
<span style="font-style:italic">Progress</span><br>
Tasks in making version 1.0:
<ul class="box">
<li> <span style="position:absolute;margin-left:-1em;">✔</span><a href="https://github.com/RickardHultgren/lympha/blob/master/LYMPHA_syntax.0.9.pdf">Syntax description in REGEX</a>; The syntax is completed.</li>
<li>Make algorithms in:</li>
<ul class="box">
<li><span style="position:relative;margin-left:-2em;">✔</span><a href="https://github.com/RickardHultgren/lympha/blob/master/LYMPHA_algorithm.0.9.pdf">pseudocode</a>; The algorithms are completed.</li>
<li><span style="position:absolute;margin-left:-3em;">&#10004;</span><a href="https://github.com/RickardHultgren/lympha/tree/python">Python</a> module; A framework for a python library is built. Now the pseudocode has to be converted into python.</li>
<li><a href="https://github.com/RickardHultgren/lympha/tree/JavaScript">JavaScript</a>; Add computational abilities to the web-browser version.</li>
</ul>
</ul>
Future plans after version 1.0:
<ul>
<li>Make a <span class="sc">lympha</span>-script client app in <a href="https://kivy.org/">Kivy</a>. This would make <span class="sc">lympha</span> very useful.</li>
<li>Make scripts for the client in the field of mental health. Anxiety and depression could both be monitored as well as treated in some gegree through <span class="sc">madrs</span> script and <span class="sc">rebt</span>. This would be a very usefull tool for first line self-help.</li>
<li>Make a <a href="https://www.gnu.org/software/gforth/">GForth</a> branch of the <span class="sc">lympha</span> project. This would enable <span class="sc">lympha</span> to be used in more smaller devices.</li>
</ul>
<br><br><br>
<a name="use" style="font-weight:bold;"></a>
<span style="font-style:italic">Use</span><br>
The finished version is thought to consolidate different protocols and compare them with data from the patient. In this way, it would enable compters to propose what further diagnostics and treatments can be prescribed. In other words, it will be a <a href="https://en.m.wikipedia.org/wiki/Clinical_decision_support_system " class="sc">cdss</a> and a programming language for medical protocols. The python version should be command based program:
<pre class="dragscroll">
$> lympha script.lympha steps=5 start="airways"
</pre>
