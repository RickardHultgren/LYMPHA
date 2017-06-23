#!/usr/bin/python3
# -*- coding: ascii -*-
import sys
precommand = ""
command = ""
argvlen = len(sys.argv)
filename = ""

filecheck = False
modeexe = False
modeshow = False
modemap = False
exe_list = []
show_list = []
map_list = []
series = []
substates = []
nextstates = []
specs = []
tipoint = None
operator = None

object_list = []
exe_objects = []

'''
class Factor:
	def __init__(self, name, tipoint, operator, next_list, spec_list, cont_list):
        		
		#list of next nodes:
		#next_list = next_list
		self.next_list = []
		
		#list of specifications:
		#spec_list = spec_list
		self.spec_list = []

		#list of contents:
		#cont_list = cont_list
		self.cont_list = []

		#name
		self.name = name
		
		#tipping point
		self.tipoint = tippoint
		
		#relational operator
		self.operator = operator

class Event:
	def __init__(self, name, next_list, spec_list, cont_list):
        		
		#list of next nodes:
		#next_list = next_list
		self.next_list = []
		
		#list of specifications:
		#spec_list = spec_list
		self.spec_list = []

		#list of contents:
		#cont_list = cont_list
		self.cont_list = []

		#name
		self.name = name
'''

class Statement:
	def __init__(self, name, tipoint, operator):
        		
		#list of next nodes:
		#next_list = next_list
		self.next_list = []
		
		#list of specifications:
		#spec_list = spec_list
		self.spec_list = []

		#list of contents:
		#cont_list = cont_list
		self.cont_list = []

		#name
		self.name = name
		
		#tipping point
		self.tipoint = tipoint
		
		#relational operator
		self.operator = operator

#object_list.append(Event(i))
#object_list.append(Factor(i))

def exefunc():
	for next_object in next_list:
		for list_object in object_list:
			if list_object == next_object:
				exe_objects.append(list_object)
	for exe_object in exe_objects:
		if exe_object.flow==1 :
			#execute exe_object
			#for subexe_object in exe_object.subobjects
				#execute subexe_object
				#pass
			exe_object = []

def showfunc():
# Add objects.name to show_list.
	global object_list
	for obj in object_list:
		for next_object in obj.next_list:
			for list_object in object_list:
				if list_object == next_object:
					exe_objects.append(list_object)
		for exe_object in exe_list:
			if exe_object.flow==1 :
				#execute exe_object
				#for subexe_object in exe_object.subobjects
					#execute subexe_object
					#pass
				exe_object = []


def mapfunc():
	for next_object in next_list:
		for list_object in object_list:
			if list_object == next_object:
				exe_objects.append(list_object)
	for exe_object in exe_objects:
		if exe_object.flow==1 :
			#execute exe_object
			#for subexe_object in exe_object.subobjects
				#execute subexe_object
				#pass
			exe_object = []



def new(name, tipoint, operator):
	statement = Statement(name, tipoint, operator)
	object_list.append(statement)

def run():
	global object_list
	for serie in series:
		manyobj = serie.split('->')
		for anobj in manyobj:
			anobj.replace(" ","")
			if anobj != "":
				new(anobj,None,None)	
	seen = {}
	object_list = [seen.setdefault(x.name, x) for x in object_list if x.name not in seen]
	if modeexe == True:
		exefunc()
		#for obj in object_list:
		#obj.next_list = ["abc"]
		#print (obj.next_list)
			#print("%s" % obj.name)	
	if modeexe == True:
		showfunc()
	if modeshow == True:
		showfunc()
	if modemap == True:
		mapfunc()
if __name__=='__main__':
	for x in range(0, argvlen):
		if sys.argv[x] == "-f":
			precommand = sys.argv[x]
			command = sys.argv[x+1]
			filename = command
			textfile = open(filename, 'r')
			filetext = textfile.read()
			filetext = filetext.replace('\n', ' ')
			filetext = filetext.replace('  ', ' ')
			series = filetext.split(';')
			filecheck = True
		if sys.argv[x] == "-h":
			print ("-h for help\n-f file")
		if sys.argv[x] == "-exe":
			modeexe = True
		if sys.argv[x] == "-show":
			modeshow = True
		if sys.argv[x] == "-map":
			modemap = True		
# Execute functions that are connected to the arguments:
	if filecheck == True:
		run()
