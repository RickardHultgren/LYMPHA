// Transcrypt'ed from Python, 2021-08-13 07:29:36
var re = {};
var sys = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {sqrt} from './math.js';
import * as __module_re__ from './re.js';
__nest__ (re, '', __module_re__);
import * as __module_sys__ from './sys.js';
__nest__ (sys, '', __module_sys__);
var __name__ = '__main__';
try {
}
catch (__except0__) {
	// pass;
}
export var preLexer = function () {
	try {
		document.body.style.backgroundColor = 'blue';
	}
	catch (__except0__) {
		// pass;
	}
	try {
		document.body.style.backgroundColor = '#ff3333';
		var theItems = document.getElementsByClassName ('theItems').value;
	}
	catch (__except0__) {
		// pass;
	}
	try {
		for (var an_item of theItems) {
			addresses.append (an_item.value);
		}
		var urls = list ();
	}
	catch (__except0__) {
		// pass;
	}
	try {
		document.body.style.backgroundColor = '#3f3';
	}
	catch (__except0__) {
		// pass;
	}
	try {
		document.body.style.backgroundColor = '#33f';
		for (var an_address of addresses) {
			urls.append (urllib.request.urlopen (an_address).read ());
		}
	}
	catch (__except0__) {
		// pass;
	}
	try {
		document.body.style.backgroundColor = '#ff3';
		for (var j of urls) {
			var filetext = j;
			var filetext = stripComments (str (filetext));
			var filetext = filetext.py_replace ('\n', ' ');
			var filetext = filetext.py_replace ('  ', ' ');
			series.extend (filetext.py_split (';'));
		}
	}
	catch (__except0__) {
		// pass;
	}
	try {
		document.body.style.backgroundColor = 'green';
		var modegraph = true;
		var modegraph = true;
		var temporary_starts = list ();
		for (var a_step of document.select ('.stepNr')) {
			var steps = a_step.value;
		}
		for (var start_item of document.select ('.theStarts')) {
			starts.append (start_item.value);
			temporary_starts.append (start_item.value);
		}
	}
	catch (__except0__) {
		// pass;
	}
};
export var recursive_parse = function (node, substitutions) {
	if (hasattr (node.left, 'id')) {
		if (__in__ (node.left.id, substitutions.py_keys ())) {
			node.left = substitutions [node.left.id];
		}
	}
	else {
		recursive_parse (node.left, substitutions);
	}
	if (hasattr (node.right, 'id')) {
		if (__in__ (node.right.id, substitutions.py_keys ())) {
			node.right = substitutions [node.right.id];
		}
	}
	else {
		recursive_parse (node.right, substitutions);
	}
};
export var CLI_filename = '';
export var argv_len = len (sys.argv);
export var filenames = list ();
export var filename = '';
export var starts = list ();
export var steps = 0;
export var local_files = true;
export var mode_graph = false;
export var mode_state = false;
export var mode_exe = false;
export var mode_show = false;
export var mode_map = false;
export var filecheck = false;
export var exe_list = list ();
export var show_list = list ();
export var map_list = list ();
export var series = list ();
export var substates = list ();
export var nextstates = list ();
export var specs = list ();
export var global_relative_variable1 = null;
export var global_relative_variable2 = null;
export var operator1 = null;
export var statement_value = str ();
export var statement_flow = 0;
export var exe_objects = list ();
export var CLIcom_segment = 0;
export var Evaluator =  __class__ ('Evaluator', [NodeVisitor], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		self._namespace = kwargs;
	});},
	get visit_Name () {return __get__ (this, function (self, node) {
		return self._namespace [node.id];
	});},
	get visit_Num () {return __get__ (this, function (self, node) {
		return node.n;
	});},
	get visit_NameConstant () {return __get__ (this, function (self, node) {
		return node.value;
	});},
	get visit_UnaryOp () {return __get__ (this, function (self, node) {
		var val = self.visit (node.operand);
		return operators [py_typeof (node.op)] (val);
	});},
	get visit_BinOp () {return __get__ (this, function (self, node) {
		var lhs = self.visit (node.left);
		var rhs = self.visit (node.right);
		return operators [py_typeof (node.op)] (lhs, rhs);
	});},
	get generic_visit () {return __get__ (this, function (self, node) {
		var __except0__ = ValueError ('malformed node or string: ' + repr (node));
		__except0__.__cause__ = null;
		throw __except0__;
	});}
});
export var Statement =  __class__ ('Statement', [dict], {
	__module__: __name__,
	MARKER: object (),
	get __init__ () {return __get__ (this, function (self, value) {
		if (typeof value == 'undefined' || (value != null && value.hasOwnProperty ("__kwargtrans__"))) {;
			var value = null;
		};
		if (value === null) {
			// pass;
		}
		else if (isinstance (value, dict)) {
			for (var key of value) {
				self.__setitem__ (key, value [key]);
			}
		}
		else {
			var __except0__ = py_TypeError ('expected dict');
			__except0__.__cause__ = null;
			throw __except0__;
		}
	});},
	get __setitem__ () {return __get__ (this, function (self, key, value) {
		if (isinstance (value, dict) && !(isinstance (value, Statement))) {
			var value = Statement (value);
		}
	});},
	get __getitem__ () {return __get__ (this, function (self, key) {
		var found = self.py_get (key, Statement.MARKER);
		if (found === Statement.MARKER) {
			var found = Statement ();
		}
		return found;
	});}
});
var __left0__ = tuple ([__setitem__, __getitem__]);
Statement.__setattr__ = __left0__ [0];
Statement.__getattr__ = __left0__ [1];
export var object_list = dict ();
var object_list = Statement (object_list);
export var mapfunc = function () {
	if (mode_graph == true) {
		var graphstr = 'digraph lympha {\nnode [shape=record];';
	}
	for (var step = 0; step < steps; step++) {
		nextstates = list ();
		for (var start of starts) {
			for (var key = 0; key < len (object_list); key++) {
				var endstring = str ();
				var strr = str (__mod__ ('%s', object_list [key].py_name));
				var strr = re.sub ('\\s+', '', strr.strip ());
				var pre_statement_flow = 1;
				if (str (start) == strr) {
					if (object_list [key].datatype == 'bina') {
						// pass;
					}
					else if (object_list [key].datatype == 'bineval' && len (object_list [key].binary_list) >= 1) {
						var pre_statement_flow = 0;
						var subfactors = list ();
						for (var binobj of object_list [key].binary_list) {
							for (var item = 0; item < len (object_list); item++) {
								var thename = object_list [item].py_name;
								var thename = str (thename);
								if (thename == __mod__ ('%s', binobj.py_replace (' ', ''))) {
									subfactors.append (int (object_list [item].statement_flow));
								}
							}
						}
						var sum1 = subfactors.count (1);
						var sum0 = subfactors.count (0);
						if (object_list [key].operator1 != null) {
							if (object_list [key].operator1 == 'equiv' && int (object_list [key].global_relative_variable1) == int (sum1)) {
								var pre_statement_flow = 1;
								object_list [key].statement_value = __mod__ ('score: %s\nthreshold: %s', tuple ([sum1, object_list [key].global_relative_variable1]));
							}
							else if (object_list [key].operator1 == 'geq' && int (object_list [key].global_relative_variable1) >= int (sum1)) {
								var pre_statement_flow = 1;
								object_list [key].statement_value = __mod__ ('score: %s\nthreshold: %s', tuple ([sum1, object_list [key].global_relative_variable1]));
							}
							else if (object_list [key].operator1 == 'leq' && int (object_list [key].global_relative_variable1) <= int (sum1)) {
								var pre_statement_flow = 1;
								object_list [key].statement_value = __mod__ ('score: %s\nthreshold: %s', tuple ([sum1, object_list [key].global_relative_variable1]));
							}
							else if (object_list [key].operator1 == 'no' && int (object_list [key].global_relative_variable1) != int (sum1)) {
								var pre_statement_flow = 1;
								object_list [key].statement_value = __mod__ ('score: %s\nthreshold: %s', tuple ([sum1, object_list [key].global_relative_variable1]));
							}
							else if (object_list [key].operator1 == 'g' && int (object_list [key].global_relative_variable1) > int (sum1)) {
								var pre_statement_flow = 1;
								object_list [key].statement_value = __mod__ ('score: %s\nthreshold: %s', tuple ([sum1, object_list [key].global_relative_variable1]));
							}
							else if (object_list [key].operator1 == 'l' && int (object_list [key].global_relative_variable1) < int (sum1)) {
								var pre_statement_flow = 1;
								object_list [key].statement_value = __mod__ ('score: %s\nthreshold: %s', tuple ([sum1, object_list [key].global_relative_variable1]));
							}
							else {
								var pre_statement_flow = 0;
							}
							print (object_list [key].statement_value);
						}
						object_list [key].statement_flow = int (pre_statement_flow);
					}
					if (object_list [key].datatype == 'nonbineval') {
						var endstring = str ();
						var string = object_list [key].statement_value.py_replace (' ', '');
						var pattern = re.compile ('([\\=\\+\\-\\/\\*\\(\\)])');
						var iteratorUntouched = re.py_split (pattern, string);
						var eqlist = list ();
						for (var varWord of iteratorUntouched) {
							print (varWord);
							var checked = 0;
							for (var objWord = 0; objWord < len (object_list); objWord++) {
								var thename = object_list [objWord].py_name;
								if (thename == varWord) {
									eqlist.append (object_list [objWord].statement_value);
									var checked = 1;
								}
							}
							if (checked == 0) {
								eqlist.append (varWord);
							}
						}
						var endstring = ''.join (eqlist);
						var endstring = str (eval (str (endstring)));
						object_list [key].statement_value = endstring;
						var endnum = float ();
						var endnum = float (eval (str (endstring)));
						var pre_statement_flow = 0;
						try {
							if (object_list [key].operator1 == 'equiv' && int (object_list [key].global_relative_variable1) == int (str (endnum))) {
								print (__mod__ ('%s == %s ; exe', tuple ([int (object_list [key].global_relative_variable1), int (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else if (object_list [key].operator1 == 'leq' && int (object_list [key].global_relative_variable1) >= int (endnum)) {
								print (__mod__ ('%s >= %s ; exe', tuple ([int (object_list [key].global_relative_variable1), int (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else if (object_list [key].operator1 == 'geq' && int (object_list [key].global_relative_variable1) <= int (str (endnum))) {
								print (__mod__ ('%s <= %s ; exe', tuple ([int (object_list [key].global_relative_variable1), int (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else if (object_list [key].operator1 == 'no' && int (object_list [key].global_relative_variable1) != int (str (endnum))) {
								print (__mod__ ('%s != %s ; exe', tuple ([int (object_list [key].global_relative_variable1), int (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else if (object_list [key].operator1 == 'g' && int (object_list [key].global_relative_variable1) < int (str (endnum))) {
								print (__mod__ ('%s < %s ; exe', tuple ([int (object_list [key].global_relative_variable1), int (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else if (object_list [key].operator1 == 'l' && int (object_list [key].global_relative_variable1) > int (str (endnum))) {
								print (__mod__ ('%s > %s ; exe', tuple ([int (object_list [key].global_relative_variable1), int (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else {
								var pre_statement_flow = 0;
							}
						}
						catch (__except0__) {
							var endnum = float (eval (str (endstring)));
							if (object_list [key].operator1 == 'equiv' && float (object_list [key].global_relative_variable1) == float (str (endnum))) {
								print (__mod__ ('%s == %s ; exe', tuple ([float (object_list [key].global_relative_variable1), float (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else if (object_list [key].operator1 == 'leq' && float (object_list [key].global_relative_variable1) <= float (endnum)) {
								print (__mod__ ('%s <= %s ; exe', tuple ([float (object_list [key].global_relative_variable1), float (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else if (object_list [key].operator1 == 'geq' && float (object_list [key].global_relative_variable1) >= float (str (endnum))) {
								print (__mod__ ('%s >= %s ; exe', tuple ([float (object_list [key].global_relative_variable1), float (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else if (object_list [key].operator1 == 'no' && float (object_list [key].global_relative_variable1) != float (str (endnum))) {
								print (__mod__ ('%s != %s ; exe', tuple ([float (object_list [key].global_relative_variable1), float (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else if (object_list [key].operator1 == 'g' && float (object_list [key].global_relative_variable1) < float (str (endnum))) {
								print (__mod__ ('%s < %s ; exe', tuple ([float (object_list [key].global_relative_variable1), float (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else if (object_list [key].operator1 == 'l' && float (object_list [key].global_relative_variable1) > float (str (endnum))) {
								print (__mod__ ('%s > %s ; exe', tuple ([float (object_list [key].global_relative_variable1), float (str (endnum))])));
								var pre_statement_flow = 1;
							}
							else {
								var pre_statement_flow = 0;
							}
						}
						object_list [key].statement_flow = int (pre_statement_flow);
					}
					if (object_list [key].datatype == 'valu') {
						var endstring = str ();
						var string = object_list [key].statement_value.py_replace (' ', '');
						var pattern = re.compile ('([\\=\\+\\-\\/\\*\\(\\)])');
						var iteratorUntouched = re.py_split (pattern, string);
						var eqlist = list ();
						for (var varWord of iteratorUntouched) {
							print (varWord);
							var checked = 0;
							for (var objWord = 0; objWord < len (object_list); objWord++) {
								var thename = object_list [objWord].py_name;
								if (thename == varWord) {
									eqlist.append (object_list [objWord].statement_value);
									var checked = 1;
								}
							}
							if (checked == 0) {
								eqlist.append (varWord);
							}
						}
						var endstring = ''.join (eqlist);
						var endstring = str (eval (str (endstring)));
						object_list [key].statement_value = endstring;
					}
					if (object_list [key].flow == 0) {
						object_list [key].statement_flow = 0;
					}
					if (mode_exe == true) {
						if (object_list [key].statement_flow == 1) {
							try {
								print (__mod__ ('Executing %s.', start));
								var cmd = __mod__ ('./%s', start);
								os.system (cmd);
							}
							catch (__except0__) {
								print (__mod__ ('Failed to executing %s.', start));
							}
						}
					}
					if (mode_graph == true) {
						if (object_list [key].statement_flow == 0) {
							var graph_string = '';
							if (object_list [key].datatype == 'bina') {
								var graph_string = '0B';
							}
							if (object_list [key].datatype == 'bineval') {
								var graph_string = object_list [key].statement_value;
							}
							if (object_list [key].datatype == 'nonbineval') {
								var graph_string = __mod__ ('score: %s', object_list [key].statement_value);
							}
							if (object_list [key].datatype == 'valu') {
								var graph_string = object_list [key].statement_value;
							}
							graphstr += __mod__ ('"%s" [label="step %s: %s\\n%s"] \n', tuple ([start, step + 1, start, graph_string]));
						}
						if (object_list [key].statement_flow == 1) {
							var graph_string = '';
							if (object_list [key].datatype == 'bina') {
								var graph_string = '1B';
							}
							if (object_list [key].datatype == 'bineval') {
								var graph_string = object_list [key].statement_value;
							}
							if (object_list [key].datatype == 'nonbineval') {
								var graph_string = __mod__ ('score: %s', object_list [key].statement_value);
							}
							if (object_list [key].datatype == 'valu') {
								var graph_string = object_list [key].statement_value;
							}
							graphstr += __mod__ ('"%s" [label="step %s: %s\\n%s", fillcolor=yellow, style=filled] \n', tuple ([start, step + 1, start, str (graph_string)]));
						}
					}
					for (var next_object of object_list [key].next_list) {
						if (mode_graph == true) {
							if (object_list [key].py_name != next_object) {
								graphstr += __mod__ ('"%s" -> "%s" \n', tuple ([start, next_object]));
							}
						}
						nextstates.append (next_object);
					}
				}
			}
		}
		nextstates = list ();
		for (var start of starts) {
			for (var k = 0; k < len (object_list); k++) {
				if (object_list [k].py_name == start) {
					for (var nexting of object_list [k].next_list) {
						for (var l = 0; l < len (object_list); l++) {
							if (object_list [l].py_name == nexting) {
								nextstates.append (nexting);
								if (object_list [k].flow == 0 || object_list [k].statement_flow == 0) {
									object_list [l].flow = 0;
								}
							}
						}
					}
				}
			}
		}
		delete starts.__getslice__ (0, null, 1);
		for (var nexting of nextstates) {
			if (!__in__ (nexting, starts)) {
				starts.append (nexting);
			}
		}
		delete nextstates.__getslice__ (0, null, 1);
	}
	if (mode_graph == true) {
		graphstr += '}';
		open ('lympha.dot', 'w').close ();
		var outputfile = open ('lympha.dot', 'w');
		outputfile.write (graphstr);
		outputfile.close ();
		var cmd = 'dot lympha.dot -Tpdf -o lympha.pdf';
		os.system (cmd);
	}
	else {
		try {
			document.log.grphstr = graphstr;
		}
		catch (__except0__) {
			// pass;
		}
	}
	CLI_filename = null;
	argv_len = null;
	filename = null;
	filenames = null;
	starts = null;
	steps = null;
	mode_graph = null;
	mode_state = null;
	filecheck = null;
	mode_exe = null;
	mode_show = null;
	mode_map = null;
	exe_list = null;
	show_list = null;
	map_list = null;
	series = null;
	substates = null;
	nextstates = null;
	specs = null;
	var global_relative_variable1 = null;
	global_relative_variable2 = null;
	var operator1 = null;
	statement_flow = null;
	statement_value = null;
	object_list = null;
	exe_objects = null;
};
export var statefunc = function () {
	for (var [key, obj] of object_list.py_items ()) {
		print (__mod__ ('%s', object_list [key].py_name));
	}
};
export var stripComments = function (code) {
	var code = str (code);
	return re.sub ('(?m)^ *#.*\\n?', '', code);
};
export var lexer = function () {
	series;
	if (local_files == true) {
		for (var afilename of filenames) {
			var textfile = open (filename, 'r');
			var filetext = textfile.read ();
			var filetext = stripComments (filetext);
			var filetext = filetext.py_replace ('\n', ' ');
			var filetext = filetext.py_replace ('  ', ' ');
			series.extend (filetext.py_split (';'));
		}
	}
	var nexts = list ();
	var conts = list ();
	for (var serie of series) {
		var prearrowobjs = serie.py_split ('->');
		var arrowobjs = list ();
		for (var anobj of prearrowobjs) {
			var almostdone = anobj.py_split ('=');
			arrowobjs.append (almostdone [0]);
		}
		var count = 0;
		var oops = str ();
		var nexts = list ();
		var conts = list ();
		var specs = list ();
		var flow = int ();
		var global_relative_variable1 = float ();
		var operator1 = str ();
		var statement_flow = int ();
		var statement_value = str ();
		var scale = list ();
		var pre_count = 0;
		var count_objs = int ();
		for (var anobj of arrowobjs) {
			var anobj = re.sub ('\\s*', '', anobj);
			var eqobjs = re.compile ('((<=)|(>=)|(!=)|(==)(<)|(>))').py_split (anobj);
			var taken = 0;
			for (var takenkey = 0; takenkey < len (object_list); takenkey++) {
				if (object_list [takenkey].py_name == anobj) {
					var taken = 1;
				}
				else {
					pre_count++;
				}
			}
			var count_objs = pre_count;
			if (anobj != '' && taken == 0) {
				object_list [count_objs].py_name = str (anobj);
				object_list [count_objs].next_list = list ();
				object_list [count_objs].binary_list = list ();
				object_list [count_objs].operation = str ('');
				object_list [count_objs].flow = 1;
				object_list [count_objs].statement_flow = 1;
				object_list [count_objs].statement_value = str ();
				object_list [count_objs].global_relative_variable1 = float ();
				object_list [count_objs].datatype = '';
			}
		}
	}
	for (var serie of series) {
		var arrowobj = serie.py_split ('->');
		var count = 0;
		var nexts = list ();
		var conts = list ();
		for (var i = 0; i < len (arrowobj); i++) {
			for (var key = 0; key < len (object_list); key++) {
				var thename = str (object_list [key].py_name);
				var thename = re.sub ('\\s*', '', thename);
				if (i != 0) {
					if (thename == arrowobj [0].py_replace (' ', '')) {
						var nexting = '';
						var nexting = arrowobj [i].py_replace (' ', '');
						if (!(nexting == '')) {
							object_list [key].next_list.append (nexting);
						}
						print (object_list [key].next_list);
						print (object_list [key].py_name);
					}
				}
			}
		}
	}
	for (var serie of series) {
		var count = 0;
		var anobj = serie;
		if (anobj != '' && __in__ (' = ', anobj)) {
			var sides = anobj.py_split (' = ');
			var side1 = sides [0];
			var side2 = sides [1];
			var side1 = side1.py_replace (' ', '');
			var side2 = side2.py_replace (' ', '');
			for (var key = 0; key < len (object_list); key++) {
				var thename = object_list [key].py_name;
				if (__mod__ ('%s', thename) == sides [0].py_replace (' ', '')) {
					if (__in__ (str ('1B'), str (sides [1]))) {
						object_list [key].statement_flow = 1;
						object_list [key].datatype = 'bina';
					}
					else if (__in__ (str ('0B'), str (sides [1]))) {
						object_list [key].statement_flow = 0;
						object_list [key].datatype = 'bina';
					}
					else if ((__in__ ('==', sides [1]) || __in__ ('!=', sides [1]) || __in__ ('<=', sides [1]) || __in__ ('>=', sides [1]) || __in__ ('<', sides [1]) || __in__ ('>', sides [1])) && !(__in__ ('->', sides [1]))) {
						if (__in__ ('==', sides [1])) {
							object_list [key].operator1 = 'equiv';
						}
						if (__in__ ('>=', sides [1])) {
							object_list [key].operator1 = 'geq';
						}
						if (__in__ ('<=', sides [1])) {
							object_list [key].operator1 = 'leq';
						}
						if (__in__ ('!=', sides [1])) {
							object_list [key].operator1 = 'no';
						}
						if (re.compile ('.*>.*').match (sides [1]) && !(re.compile ('(>=)').match (sides [1]))) {
							object_list [key].operator1 = 'g';
						}
						if (re.compile ('.*<.*').match (sides [1]) && !(re.compile ('(<=)').match (sides [1]))) {
							object_list [key].operator1 = 'l';
						}
						print (object_list [key].operator1);
						var preop = sides [1].py_replace (' ', '');
						var bin_chopped = 0;
						if (__in__ ('\\|{', preop) || __in__ ('|{', preop)) {
							var bin_chopped = 1;
						}
						var preop = re.sub ('(\\|{)', ' ', preop);
						var preop = re.sub ('(}\\|)', ' ', preop);
						var chopcompile = re.compile ('(<=|>=|!=|==|<|>)');
						var operator_chop = re.py_split (chopcompile, preop);
						print (operator_chop);
						var zerochop = operator_chop [0].py_replace (' ', '');
						object_list [key].global_relative_variable1 = zerochop;
						if (bin_chopped == 1) {
							var binary_sums = list (operator_chop [2].py_split (','));
							for (var binary of binary_sums) {
								var binary = binary.py_replace (' ', '');
								if (binary != '') {
									var binary = str (binary.py_replace (' ', ''));
									object_list [key].binary_list.append (str (binary));
								}
								object_list [key].datatype = 'bineval';
							}
						}
						else if (bin_chopped == 0) {
							object_list [key].statement_value = operator_chop [2];
							object_list [key].datatype = 'nonbineval';
						}
					}
					else if (sides [0] != '' && sides [1] != '') {
						print (__mod__ ('YYY %s', object_list [key].py_name));
						object_list [key].statement_value = sides [1];
						object_list [key].datatype = 'valu';
					}
				}
				print (__mod__ ('DATA TYPE: %s', object_list [key].datatype));
			}
		}
	}
	if (mode_graph == true || mode_exe == true) {
		mapfunc ();
	}
};
if (__name__ == '__main__') {
	for (var x = 0; x < argv_len; x++) {
		if (sys.argv [x] == '-f') {
			var CLI_filename = sys.argv [x + 1];
			var filename = CLI_filename;
			filenames.append (filename);
			var filecheck = true;
		}
		if (sys.argv [x] == '-h') {
			print ('-h for help\n-f file\n-graph\n-start "start node"\n-steps amount of steps');
		}
		if (sys.argv [x] == '-exe') {
			var mode_exe = true;
		}
		if (sys.argv [x] == '-graph') {
			var mode_graph = true;
		}
		if (sys.argv [x] == '-statements') {
			var mode_state = true;
		}
		if (sys.argv [x] == '-steps') {
			var steps = int (sys.argv [x + 1]);
		}
		if (sys.argv [x] == '-start') {
			starts.append (sys.argv [x + 1]);
		}
	}
	if (filecheck == true) {
		lexer ();
	}
	else {
		print ('Please add file names.');
	}
}

//# sourceMappingURL=lympha.map