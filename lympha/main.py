#!/usr/bin/python3
# -*- coding: ascii -*-
import sys

#for the graph function:
import os

#regex
import re

prefilecom = ""
filecom = ""
argvlen = len(sys.argv)
filename = ""

starts = list()
steps = 0
modegraph = False
modestate = False
filecheck = False
modeexe = False
modeshow = False
modemap = False
exe_list = list()
show_list = list()
map_list = list()
series = list()
substates = list()
nextstates = list()
specs = list()
tipoint = None
operator = None
valju = int()

object_list = list()
exe_objects = list()

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
	def __init__(self, name, valju, tipoint, operator, next_list, cont_list, spec_list):
        
		self.flow = False
        		
		#list of next nodes:
		#next_list = next_list
		self.next_list = list(next_list)
		
		#list of specifications:
		#spec_list = spec_list
		self.spec_list = list()

		#list of contents:
		#cont_list = cont_list
		self.cont_list = list(cont_list)

		#name
		self.name = name
		
		#tipping point
		self.tipoint = tipoint
		
		#relational operator
		self.operator = operator

		#valju
		#if valju != 0 :print (valju)
		if valju == 0 :self.valju = 0
		else: self.valju = 1
		#if self.valju != 0 :print ("%s:%s" % (self.name, self.valju))

#object_list.append(Event(i))
#object_list.append(Factor(i))

def exefunc() :
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	
	
	
	if modegraph == True:
		graphstr = 'digraph lympha {\nnode [shape=record];'	
	for step in range(0,steps):
		nextstates = list()
		for start in starts:
			#for index,obj in enumerate(object_list):
			for obj in object_list:
				if ("%s" % obj.name) == ("%s" % start) :
					subfactors = list()
					for cont_object in obj.cont_list :
						for item in object_list:							
							if cont_object == item.name :
								subfactors.append(item.valju)
					print("SUBFACTORS: %s"%subfactors)
					sum1 = subfactors.count(1)
					sum0 = subfactors.count(0)
					print("sum1:%s"%subfactors)
					print("nanme:%s ; topioint:%s ; operator:%s ; obj.tipoint:%s" %(obj.name, obj.tipoint, obj.operator, obj.tipoint))
					if obj.operator	!= None and obj.valju is None :
						if obj.operator == "equiv" and obj.tipoint == sum1:
							obj.valju = 1
						elif obj.operator == "geq" and obj.tipoint >= sum1:
							obj.valju = 1
						elif obj.operator == "leq" and obj.tipoint <= sum1:
							obj.valju = 1
						elif obj.operator == "no" and obj.tipoint != sum1:
							obj.valju = 1
						elif obj.operator == "g" and obj.tipoint > sum1:
							obj.valju = 1
						elif obj.operator == "l" and obj.tipoint < sum1:
							print (sum1)
							obj.valju = 1
						else:
							obj.valju = 0	
					#else:
						#obj.valju = 1	
###connect to funcs


					if obj.valju == 1:
						print ("step %s: %s; exe" % (step+1, start))
					else:
						print ("step %s: %s"% (step+1, start))
					
					
					if modegraph == True:
						if obj.valju == 1:
							graphstr += ('"%s" [label="step %s: %s", fillcolor=yellow, style=filled] \n' % (start,step+1,start))										
						else:
							graphstr += ('"%s" [label="step %s: %s"] \n' % (start,step+1,start))										
					for next_object in obj.next_list :
						if obj.name != next_object and start != next_object and step != steps-1:
							graphstr += ('"%s" -> "%s" \n' % (start,next_object))
							nextstates.append(next_object)
		seen2 = {}
		nextstates = [seen2.setdefault(x, x) for x in nextstates if x not in seen2]
		del starts[:]
		starts = list(nextstates)
		del nextstates[:]
	graphstr += '}'
	open('lympha.dot', 'w').close()
	outputfile = open("lympha.dot", "w")
	outputfile.write(graphstr)
	outputfile.close()
	cmd = 'dot lympha.dot -Tps -o lympha.pdf'
	os.system(cmd)


def showfunc():
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	if modegraph == True:
		graphstr = 'digraph lympha {\nnode [shape=record];'
	for step in range(0,steps):
		nextstates = list()
		for start in starts:
			for obj in object_list:
				if ("%s" % obj.name) == ("%s" % start) :
					print ("step %s: %s" % (step+1, start))
					if modegraph == True:
						graphstr += ('"%s" [label="step %s: %s"] \n' % (start,step+1,start))					
					for next_object in obj.next_list :
						if obj.name != next_object and start != next_object and step != steps-1:
							graphstr += ('"%s" -> "%s" \n' % (start,next_object))
							nextstates.append(next_object)
		seen2 = {}
		nextstates = [seen2.setdefault(x, x) for x in nextstates if x not in seen2]
		del starts[:]
		starts = list(nextstates)
		del nextstates[:]
	graphstr += '}'
	open('lympha.dot', 'w').close()
	outputfile = open("lympha.dot", "w")
	outputfile.write(graphstr)
	outputfile.close()
	cmd = 'dot lympha.dot -Tps -o lympha.pdf'
	os.system(cmd)

def mapfunc():
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	
	
	
	if modegraph == True:
		graphstr = 'digraph lympha {\nnode [shape=record];'	
	for step in range(0,steps):
		nextstates = list()
		for start in starts:
			#for index,obj in enumerate(object_list):
			for obj in object_list:
				if ("%s" % obj.name) == ("%s" % start) :
					if len(obj.cont_list) != 0 :
						subfactors = list()
						for cont_object in obj.cont_list :
							for item in object_list:							
								if cont_object == item.name :
									#if item.name != "":
									#	print("name: %s ; value: %s"%(item.name, item.valju))
									subfactors.append(item.valju)
						sum1 = subfactors.count(1)
						sum0 = subfactors.count(0)
						if obj.operator	!= None and obj.valju is None :
							if obj.operator == "equiv" and obj.tipoint == sum1:
								obj.valju = 1
							elif obj.operator == "geq" and obj.tipoint >= sum1:
								obj.valju = 1
							elif obj.operator == "leq" and obj.tipoint <= sum1:
								obj.valju = 1
							elif obj.operator == "no" and obj.tipoint != sum1:
								obj.valju = 1
							elif obj.operator == "g" and obj.tipoint > sum1:
								obj.valju = 1
							elif obj.operator == "l" and obj.tipoint < sum1:
								print (sum1)
								obj.valju = 1
							else:
								obj.valju = 0	
						#else:
							#obj.valju = 1	
					###
					#algorithm algebra:
					else:
						
						for algobj in object_list:
						
							if  algobj == ("%s" % obj.valju):
								sum1 = ("%s" % obj.valju)
						if obj.operator	!= None and obj.valju is None :
							if obj.operator == "equiv" and obj.tipoint == sum1:
								obj.valju = 1
							elif obj.operator == "geq" and obj.tipoint >= sum1:
								obj.valju = 1
							elif obj.operator == "leq" and obj.tipoint <= sum1:
								obj.valju = 1
							elif obj.operator == "no" and obj.tipoint != sum1:
								obj.valju = 1
							elif obj.operator == "g" and obj.tipoint > sum1:
								obj.valju = 1
							elif obj.operator == "l" and obj.tipoint < sum1:
								print (sum1)
								obj.valju = 1
							else:
								obj.valju = 0	
						#else:
							#obj.valju = 1							


					print("name:%s\nvalue:%s" % (obj.name,obj.valju))
					if obj.valju == 1:
						print ("step %s: %s; exe" % (step+1, start))
					else:
						print ("step %s: %s"% (step+1, start))
					
					if modegraph == True:
						if obj.valju == 1:
							graphstr += ('"%s" [label="step %s: %s", fillcolor=yellow, style=filled] \n' % (start,step+1,start))										
						else:
							graphstr += ('"%s" [label="step %s: %s"] \n' % (start,step+1,start))										
					for next_object in obj.next_list :
					
						if obj.name != next_object and start != next_object and step != steps-1:
							graphstr += ('"%s" -> "%s" \n' % (start,next_object))
							nextstates.append(next_object)
		seen2 = {}
		nextstates = [seen2.setdefault(x, x) for x in nextstates if x not in seen2]
		del starts[:]
		starts = list(nextstates)
		del nextstates[:]
	graphstr += '}'
	open('lympha.dot', 'w').close()
	outputfile = open("lympha.dot", "w")
	outputfile.write(graphstr)
	outputfile.close()
	cmd = 'dot lympha.dot -Tps -o lympha.pdf'
	os.system(cmd)

def statefunc():
	global object_list
	for obj in object_list:
		print("%s" % obj.name)	



def new(name, tipoint, valju, operator, next_list, cont_list, spec_list):
	#if valju != 0:
	#			print(valju)
	#print(valju)
	global object_list
	nameused = False
	for index, obj in enumerate(object_list):
		
		if (" %s " % obj.name) == name:
			#print("| %s |;|%s|" % (obj.name,name))
			nameused = True
			if tipoint is None:
				object_list[index].tipoint == tipoint
			if valju is None:
				
				object_list[index].valju == valju
				if valju != 0: print("%s:%s\n" % (object_list[index].valju, valju))
			if operator != None:
				object_list[index].operator == operator				
			if next_list != None:
				object_list[index].next_list == next_list				
			if cont_list != None:
				object_list[index].cont_list == cont_list
			if spec_list != None:
				object_list[index].spec_list == spec_list								
	if nameused == False:
		#if valju != 0: print("%s:%s\n" % (object_list[index].valju, valju))
		name = name.replace(' ', '')
		#if valju !=0 :print(valju)
		statement = Statement(name, tipoint, valju, operator, next_list, cont_list, spec_list)
		#statement = Statement(name, tipoint, operator, list(next_list), cont_list, spec_list)
		#if next_list != [] :
		#	statement.next_list = list(next_list)
		#if cont_list != [] :
		#	pass
		object_list.append(statement)

def assasement(eqobjs):
	#0 = operator
	#1 = tipping point
	#2 = content
	try:
		scale = eqobjs.split('==')
		scale.insert(0, "equiv")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('>=')
		scale.insert(0, "geq")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('<=')
		scale.insert(0, "leq")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('!=')
		scale.insert(0, "no")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('>')
		scale.insert(0, "g")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('<')
		scale.insert(0, "l")
		return eqobjs
		#break
	except:
		pass


def lexer():
#loop problem in the same serie
	global object_list

	nexts = list()
	conts = list()
	#make new nodes in database
	for serie in series:
		arrowobjs = serie.split('->')
		count = 0
		nexts = list()
		conts = list()
		specs = list()
		tipoint = int()
		operator = str()
		valju = int()
		scale = list()
		for anobj in arrowobjs:
###
			#eqobjs = anobj.split(' = ',1)
			#anobj.replace(" ","")
			eqobjs = re.compile("[^=|<|>|!]=[^=|<|>|!]").split(anobj)

			anobj.replace(" ","")
			new(eqobjs[0],tipoint, int(valju), operator,nexts,conts, specs)			
	seen = {}
	object_list = [seen.setdefault(x.name, x) for x in object_list if x.name not in seen]
	#Connect the database nodes
	for serie in series:
		arrowobj = serie.split('->')
		count = 0
		nexts = list()
		conts = list()
		# many nexts vs one
		for i in range(len(arrowobj)):
		#for anobj in arrowobj:
			#print (arrowobj[i]):
			for bnobj in object_list :
				if i!=0 and (" %s " % bnobj.name) == ("%s" % arrowobj[(i-1)]):
					nexting = ""
					nexting = arrowobj[i].replace(" ","")
					if not nexting == "":
						bnobj.next_list.append(nexting)
			seen3 = {}
			bnobj.next_list = [seen3.setdefault(x, x) for x in bnobj.next_list if x not in seen3]
			
			
	for serie in series:
		count = 0
		# many nexts vs one
		anobj = serie
		
		if anobj != "" and " = " in anobj:
			for bnobj in object_list :
				#Valju or tipoint
				#sides =	anobj.split(' = ')
				sides = re.compile("[^=|<|>|!]=[^=|<|>|!]").split(anobj)
				side1 = sides[0]
				side1 = side1.replace(" ","")
				
				if side1 == bnobj.name :
					parts = sides[1]
					parts = parts.replace(" ","")
					if parts.isdigit() == True:	
						bnobj.valju = int(parts)
					else:
						subfactorings = []
						if "==" in parts :
							subfactorings = parts.split("==",1)
							bnobj.operator="equiv"
						elif "=>" in parts :
							subfactorings = parts.split("=>",1)
							bnobj.operator="geq"						
						elif "=<" in parts :
							subfactorings = parts.split("=<",1)
							bnobj.operator="gleq"
						elif "!=" in parts :
							subfactorings = parts.split("!=",1)
							bnobj.operator="no"
						elif ">" in parts :
							subfactorings = parts.split(">",1)
							bnobj.operator="g"
						elif "<" in parts :
							subfactorings = parts.split("<",1)
							bnobj.operator="l"
						partlist = subfactorings[1].split(",")
						
						if re.match(r"\|\{A-Za-z0-9.,:-\s]*\}\|", parts):
							parts = parts.replace("|{","")
							parts = parts.replace("}|","")
							for party in partlist:
								bnobj.cont_list.append(party)
								bnobj.valju = None
						else:
						#elif len(partlist) == 2 :
						###
							print("\n\n\n\n\n%s"%subfactorings[1])
							bnobj.valju = [str(s) for s in sides[1].split()][1]
							
					sidelist = [int(s) for s in sides[1].split() if s.isdigit()]
					try:
						bnobj.tipoint = sidelist[0]								
					except:
							pass						
						
				
	#seen = {}
	#object_list = [seen.setdefault(x.name, x) for x in object_list if x.name not in seen]			

	if modeexe == True:
		exefunc()	
	if modeshow == True:
		showfunc()
	if modemap == True:
		mapfunc()
	if modestate == True:
		statefunc()	
if __name__=='__main__':
	for x in range(0, argvlen):
		if sys.argv[x] == "-f":
			prefilecom = sys.argv[x]
			filecom = sys.argv[x+1]
			filename = filecom
			textfile = open(filename, 'r')
			filetext = textfile.read()
			filetext = filetext.replace('\n', ' ')
			filetext = filetext.replace('  ', ' ')
			series = filetext.split(';')
			filecheck = True
		if sys.argv[x] == "-h":
			print ('-h for help\n-f file\n-map OR -show\n-graph\n-start "start node"\n-steps amount of steps')
		if sys.argv[x] == "-exe":
			modeexe = True
		if sys.argv[x] == "-show":
			modeshow = True
		if sys.argv[x] == "-map":
			modemap = True		
		if sys.argv[x] == "-graph":
			modegraph = True					
		if sys.argv[x] == "-statements":
			modestate = True	
		if sys.argv[x] == "-steps":
			steps = int(sys.argv[x+1])
		if sys.argv[x] == "-start":
			starts.append(sys.argv[x+1])
# Execute functions that are connected to the arguments:
	if filecheck == True:
		lexer()

#i? = j? = k?
