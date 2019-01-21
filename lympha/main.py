#!/usr/bin/python3
# -*- coding: ascii -*-
import sys

#for the graph function:
import os

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
			#for index, obj in enumerate(object_list):
			for obj in enumerate(object_list):
				if ("%s" % obj.name) == ("%s" % start) :

					#Sum all content-objs:
					for cont_object in obj.cont_list :
						# Critical list of trues???
						truefalse = True
						subfactors = list()
						
						
						
						try:
							arrowobjs = cont_object.replace(' ', '')
							#colonobjs = arrowobjs.split(':',1)						
							if colonobjs[0] == "T" : truefalse = True
							elif colonobjs[0] == "F" : truefalse = False
							else: print ("error")
							subfactors = colonobjs[1].split(",")
							for subfactor in subfactors:
								name = name.replace(' ', '')
								if subfactor != "T" or subfactor != "F" :
									identities = list(assasement(subfactor))
									#identities[0]
									for obj2 in object_list:
										if identities[1] == obj2.name:
											try:
												identities[1]=int(obj2.valju)
											except:
												print("Statement %s has no valju." % obj2.name)
										if identities[2] == obj2.name:
											try:
												identities[2]=int(obj2.valju)
											except:
												print("Statement %s has no valju." % obj2.name)
										if identities[0] == "equiv" and identities[1] == identities[2]:
											subfactor = "T"
										else:
											subfactor = "F"
										if identities[0] == "geq" and identities[1] >= identities[2]:
											subfactor = "T"
										else:
											subfactor = "F"											
										if identities[0] == "leq" and identities[1] <= identities[2]:
											subfactor = "T"
										else:
											subfactor = "F"											
										if identities[0] == "no" and identities[1] != identities[2]:
											subfactor = "T"
										else:
											subfactor = "F"											
										if identities[0] == "g" and identities[1] > identities[2]:
											subfactor = "T"
										else:
											subfactor = "F"											
										if identities[0] == "l" and identities[1] < identities[2]:
											subfactor = "T"
										else:
											subfactor = "F"
									if truefalse == True:
										subcount = subfactors.count("T")
									elif truefalse == False:
										subcount = subfactors.count("F")			


							#print("operator:%s\n" % obj.operator)
							if obj.operator == "equiv"	!= None:
								if obj.operator == "equiv" and identities[1] == subfactors:
									object_list[index].valju = 1
								else:
									object_list[index].valju = 0
								if obj.operator == "geq" and identities[1] >= subfactors:
									object_list[index].valju = 1
								else:
									object_list[index].valju = 0			
								if obj.operator == "leq" and identities[1] <= subfactors:
									object_list[index].valju = 1
								else:
									object_list[index].valju = 0			
								if obj.operator == "no" and identities[1] != subfactors:
									object_list[index].valju = 1
								else:
									object_list[index].valju = 0			
								if obj.operator == "g" and identities[1] > subfactors:
									object_list[index].valju = 1
								else:
									object_list[index].valju = 0			
								if obj.operator == "l" and identities[1] < subfactors:
									object_list[index].valju = 1
								else:
									object_list[index].valju = 0	

						except:
							pass


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
					for cont_object in obj.cont_list :
						# Critical list of trues???
						truefalse = True
						subfactors = list()
						
						for item in object_list:
							#print("name: %s ; value: %s"%(item.name, item.valju))
							if cont_object == item.name :
								print ("item name:%s value:%s"%(item.name, item.valju))
								subfactors.append(item.valju)
						sum1 = subfactors.count(1)
						sum0 = subfactors.count(0)
						#print("sum1:%s"%sum1)
						#print("op:%s"%obj.operator)
						if obj.operator	!= None:
							#print("????sum1:%s"%sum1)
							if obj.operator == "equiv" and sum1 == obj.tipoint:
								obj.valju = 1
							else:
								obj.valju = 0
							if obj.operator == "geq" and sum1 >= obj.tipoint:
								obj.valju = 1
							else:
								obj.valju = 0			
							if obj.operator == "leq" and sum1 <= obj.tipoint:
								obj.valju = 1
							else:
								obj.valju = 0			
							if obj.operator == "no" and sum1 != obj.tipoint:
								obj.valju = 1
							else:
								obj.valju = 0			
							if obj.operator == "g" and sum1 > obj.tipoint:
								obj.valju = 1
							else:
								obj.valju = 0			
							if obj.operator == "l" and sum1 < obj.tipoint:
								obj.valju = 1
							else:
								obj.valju = 0		

					#print("operator:%s\n" % obj.operator)
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
			if tipoint != None:
				object_list[index].tipoint == tipoint
			if valju != None:
				
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


def run():
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
		# many nexts vs one
		scale = list()
		for anobj in arrowobjs:
			anobj.replace(" ","")
			eqobjs = anobj.split('=',1)
			try:
				anobj.replace(" ","")
				if eqobjs[1].isdigit() == True :
					#print(eqobjs[1])
					valju = int(eqobjs[1])
					#print(valju)
				else:
					scale = list(assasement(eqobjs[1]))
					tipoint = scale[1]
					# delete first two and last two characters in scale[1] by [2:-2]:
					scale = scale[2][2:-2]
					conts = scale.split(",")
					
					if scale[0] == "equiv":
						thesum = subs.count(True)
						operator = scale[0]
						tipoint = scale[1]
						pass
					if scale[0] == "geq":
						thesum = subs.count(True)
						operator = scale[0]
						tipoint = scale[1]
						pass
						
					if scale[0] == "leq":
						thesum = subs.count(True)
						operator = scale[0]
						tipoint = scale[1]
						pass
						
					if scale[0] == "g":
						thesum = subs.count(True)
						operator = scale[0]
						tipoint = scale[1]
						pass
						
					if scale[0] == "l":
						thesum = subs.count(True)
						operator = scale[0]
						tipoint = scale[1]
						pass
						
					if scale[0] == "no":
						thesum = subs.count(True)
						operator = scale[0]
						tipoint = scale[1]
						pass
						
			except:
				pass
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
		for anobj in arrowobj:
			anobj.replace(" ","")
			if not anobj == "" :
				for bnobj in object_list :


					
							#if sides[1] has pattern ]{???}] = cont_list
					#critical:
					if (" %s " % bnobj.name) == ("%s" % anobj):
						nexting = ""
						try:
							newcount=count+1
							#nexting = arrowobj[newcount].replace(" ","")
							nexting = arrowobj[1].replace(" ","")
							if not nexting == "":
								#nexts.append(nexting)
								#bnobj.next_list += nexts
								bnobj.next_list.append(nexting)
								#print( "obj.next_list:%s" % bnobj.next_list )
								#nexts = []
								#nexting = ""
						except:
							pass
					seen3 = {}
					bnobj.next_list = [seen3.setdefault(x, x) for x in bnobj.next_list if x not in seen3]
				
				count += 1
			count = 0
			
			
	for serie in series:
		count = 0
		# many nexts vs one
		anobj = serie
		if anobj != "" and " = " in anobj:
			
			for bnobj in object_list :
				#Valju or tipoint					
				sides =	anobj.split(' = ')
				if sides[0] == bnobj.name :
					
					#check if sides[2] has pattern ]{???}] = cont_list
					parts = ""
					try:
						parts = sides[1].replace("|{","")
						parts = parts.replace("}|","")
						#parts = parts.replace(" ","")
					except:
						pass
					subfactorings = []
					if "==" in parts :
						subfactorings = parts.split("==",1)
						parts=subfactorings[1]
						bnobj.operator="equiv"
					elif "=>" in parts :
						subfactorings = parts.split("=>",1)
						parts=subfactorings[1]
						bnobj.operator="geq"							
					elif "=<" in parts :
						subfactorings = parts.split("=<",1)
						parts=subfactorings[1]
						bnobj.operator="gleq"
					elif "!=" in parts :
						subfactorings = parts.split("!=",1)
						parts=subfactorings[1]
						bnobj.operator="no"
					elif ">" in parts :
						subfactorings = parts.split(">",1)
						parts=subfactorings[1]
						bnobj.operator="g"
					elif "<" in parts :
						subfactorings = parts.split("<",1)
						parts=subfactorings[1]
						bnobj.operator="l"
			
					#print ("parts %s"%parts)
					try:
						parts = parts.replace(" ","")
						if parts == "T":
							print("%s True"%bnobj.name)
							bnobj.valju = 1
						elif parts == "F":
							print("%s False"%bnobj.name)
							bnobj.valju = 0	
						else:
							partlist = parts.split(",")
							for part in partlist:
								part = part.replace(" ","")
								if part != "" or part != " ":
									bnobj.cont_list.append(part)
									#print("contlist %s"%bnobj.cont_list)
									#print ("subs: %s"  % part)
						#print (bnobj.valju)
						sidelist = [int(s) for s in sides[1].split() if s.isdigit()]
						bnobj.tipoint = sidelist[0]								
							
						print ("operator: %s"  % bnobj.operator)
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
		run()
		
#What valju do do the content parts have?
		
