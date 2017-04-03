<script>
document.getElementById( "demosmall").style.backgroundColor="#EFAB00";
document.getElementById( "demotext").style.color="#000000";
document.getElementById( "demo").className="menu2active";
</script>
<script>

function storageAvailable(type) {
    try {
        var storage = window[type],
            x = '__storage_test__';
        storage.setItem(x, x);
        storage.removeItem(x);
        return true;
    }
    catch(e) {
        return false;
    }
}
var listarray = ["head"];
if (storageAvailable('localStorage')) {
    // Yippee! We can use localStorage awesomeness
    var listdot = JSON.parse(localStorage.getItem("listdot"));
	//alert(listdot);
	if (listdot!=""){
		listarray = listdot.split(",");
	}
    var longus = listarray.length;
}
else {
    // Too bad, no localStorage for us
    //var list = new LinkedList();
}
</script>	
<script>
var listnew = "";
var subarray = [];
function reloading(){
	if (listnew!=""){
		listarray.push(listnew);
	}
	var listdot = listarray.join(",");
	localStorage.setItem("listdot", JSON.stringify(listdot));
	location.reload(); 
}
</script>	
<script>
function New(){
	var listdot = "";
	localStorage.setItem("listdot", JSON.stringify(listdot));
	location.reload(); 
}
	
</script>
	
<p style="text-align:left;">
	<span class="sc">Lympha</span> javascript demo:<br>
	<br>
<div class="button" onclick="New();" style="margin-bottom:1.75em;">
new algorithm
</div>
<form id="myForm"  method="post" style="margin:0 0 .25em 0;">
            <input class="inputing" type='text' id="id" name='id' value='enter_node_name' />&nbsp;
            <input class="button" type='submit' name='submit' value='add node' onclick='addParam()' />
        </form>
</p>
<p style="border:0.1em solid #cccccc;padding:0.5em;">
	List of nodes:<br>
	<script> 
	function addParam() {
		listnew = document.getElementById('id').value;
		
		reloading();
	}
	
	function addSub(i, subString) {
		//var subarray=listarray[i].split(";");
		listarray[i] = listarray[i] + ';' + document.getElementById(subString).value;
		reloading();
	}
	
	function showSub(i) {
		subs = "<div id='input2Sub"+i+"' style='display:none;'>";
		subarray=listarray[i].split(";");
		for (var j = 0; j < subarray.length; j++) {
			if (j!=0){
				if(subarray[j]){
					subs = subs + '&nbsp;&nbsp;&nbsp;' + subarray[j] + '&nbsp;<span class="button" href="javascript:void(0);" title="delete" onclick="subarray=listarray['+i+'].split(\';\');subarray.splice('+j+', '+j+');listarray['+i+']=subarray.join(\';\');reloading();">delete</span><br>';
				}
			}
			
		}
		subs = subs + "</div>";
	}
var subs = '';
	</script>	

<span id="status">
<script>
for (var i = 0; i < listarray.length; i++) {
	if (i!=0){
		var theName;
		var newdiv = document.createElement('div');
		var subarray=listarray[i].split(";");
		for (var j = 0; j < subarray.length; j++) {
			if (j==0){
				theName = subarray[j];
			}
		}
		showSub(i);
		newdiv.innerHTML = '<div style="padding:0.5em;background-color:#cccccc;width:97.5%;margin-bottom:0.66em;">' + theName + ' &nbsp;<div class="button" style="" onclick="showhide(\'arrowright'+i+'\');showhide(\'arrowdown'+i+'\');showhide(\'inputSub'+i+'\');showhide(\'input2Sub'+i+'\');">pointing to nodes&nbsp;&nbsp;<span id="arrowright'+i+'" style="font-style:normal;font-weight:bold;">&gt;</span><span id="arrowdown'+i+'" style="font-style:normal;font-weight:bold;display:none;">v</span></div><div class="button" style="float:right" href="javascript:void(0);" title="delete" onclick="listarray.splice('+i+', '+i+');reloading();">delete</div><br><div id="inputSub'+i+'" style="display:none;border:0.1em solid #777777; padding:0.25em;">' + subs + '<form style="display:style="display:inline-block;"  method="post"><input class="inputing" type="text" id="id'+i+'" name="id'+i+'" value="enter_node_name" />&nbsp;&nbsp;<input type="submit" name="submit" class="button" value="add new connection" onclick="addSub('+i+',\'id'+i+'\')" /></form></div></div>';
		document.getElementById('status').appendChild(newdiv);
	}
}		

</script>
<script>
function showhide(k){
	if(document.getElementById(k).style.display == 'none')
		{document.getElementById(k).style.display = 'inline-block';
		}else{document.getElementById(k).style.display = 'none';
	}
}

</script>
</span>
</p>
<p style="text-align:center;margin-top:.75em;">
flow-chart representation:
</p>
<p id="status2" style="text-align:center;border:0.2em solid #cccccc;margin:0em 20.5vw 0.5em 20.5vw;"></p>


    <script src="./viz.js"></script>
    <script>
    var theGraph = "";
    for (var i = 0; i < listarray.length; i++) {
		if (i!=0){
			var subarray=listarray[i].split(";");
			theGraph = theGraph + subarray[0] + ";";				
			for (var j = 0; j < subarray.length; j++) {
				if (j!=0){
					if(subarray[j]){
						theGraph = theGraph + subarray[0] + " -> " + subarray[j] + ";";
					}
				}
			}
		}
	}

![Alt text](https://g.gravizo.com/source/custom_mark10?https%3A%2F%2Fraw.githubusercontent.com%2FTLmaK0%2Fgravizo%2Fmaster%2FREADME.md)
<details> 
<summary></summary>
custom_mark10
  digraph G {
    aize ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf};
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }
custom_mark10
</details>
    
