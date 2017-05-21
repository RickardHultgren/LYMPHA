<script>
document.getElementById( "aboutsmall").style.backgroundColor="#EFAB00";
document.getElementById( "abouttext").style.color="#000000";
document.getElementById( "about").className="menu2active";
</script>
<span class="sc">Lympha</span> is a logical language for formulating and handling medical algorithms. The aim of the project is to provide syntax guide lines as well as structural rules for reading <span class="sc">lympha</span> scripts. Interpreters and compilers are built upon those rules. The <span class="sc">lympha</span> project is open-source, licensed under the <span class="sc">[bsd 2](http://opensource.org/licenses/BSD-2-Clause)</span> license.<br><br>
<br><br><br>
<a name="progress" style="font-weight:bold;"></a>
<span style="font-style:italic">Progress</span><br>
Tasks in making version 1.0:
<ul class="task-list">
<li class="task-list-item"> <label class="task-list-control"><input type="checkbox" disabled="" checked="" /><span class="task-list-indicator"></span><a href="https://github.com/RickardHultgren/lympha/blob/master/LYMPHA_syntax.0.1.pdf">Syntax description in REGEX</a>. The syntax is completed.</label></li>
<li>Make compute algorithms in:</li>
<ul class="task-list">
<li class="task-list-item"> <label class="task-list-control"><input type="checkbox" disabled="" checked="" /><span class="task-list-indicator"></span><a href="https://github.com/RickardHultgren/lympha/blob/master/LYMPHA_algorithm.0.1.pdf">pseudocode</a><br>The algorithms are completed.</label></li>
<li class="task-list-item"> <label class="task-list-control"><input type="checkbox" disabled="" /><span class="task-list-indicator"></span><a href="https://github.com/RickardHultgren/lympha/tree/python">Python</a> modul. A framework for a python library is built. Now the pseudocode has to be converted into python.</label></li>
<li class="task-list-item"> <label class="task-list-control"><input type="checkbox" disabled="" /><span class="task-list-indicator"></span><a href="https://github.com/RickardHultgren/lympha/tree/JavaScript">JavaScript</a>. Add computational abilites to the web-browser version.</label></li>
</ul>
</ul>
Future plans after version 1.0:
<ul>
<li>Make a <span class="sc">lympha</span>-script client app in <a href="https://kivy.org/">Kivy</a>. This would make <span class="sc">lympha</span> very usefull.</li>
<li>Make scripts for the client in the field of mental health. Anxiety and depression could both be monitored as well as treated in some gegree through <span class="sc">madrs</span> script and <span class="sc">rebt</span>. This would be a very usefull tool for first line selfhelp.</li>
<li>Make a <a href="https://www.gnu.org/software/gforth/">GForth</a> branch of the <span class="sc">lympha</span> project. This would enable <span class="sc">lympha</span> to be used in more smaller devices.</li>
</ul>
<br><br><br>
<a name="use" style="font-weight:bold;"></a>
<span style="font-style:italic">Use</span><br>
The python version should be command based porgram:
<pre class="dragscroll">
$> lympha script.lympha steps=5 start="airways"
</pre>
