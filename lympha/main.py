#!/usr/bin/python3
# -*- coding: ascii -*-
import sys
prefilecom = ""
filecom = ""
argvlen = len(sys.argv)
filename = ""

starts = []
steps = 0
modegraph = False
modestate = False
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
	def __init__(self, name, tipoint, operator, next_list, cont_list, spec_list):
        
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

#object_list.append(Event(i))
#object_list.append(Factor(i))

def exefunc():
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	nextstates = []
	for step in range(0,steps):
		for start in starts:
			for obj in object_list:
				if ("%s" % obj.name) == ("%s" % start):
					print ("step %s: %s" % (step, start))
					
					for next_object in obj.next_list:
						
						nextstates.append(next_object)
			start = list()			
			seen2 = {}
			nextstates = [seen2.setdefault(x, x) for x in nextstates if x not in seen2]
			starts = list(nextstates)
			nextstates = list()

def showfunc():
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	nextstates = []
	for step in range(0,steps):
		for start in starts:
			for obj in object_list:
				if ("%s" % obj.name) == ("%s" % start):
					print ("step %s: %s" % (step, start))
					if modegraph == True:
						print ("graph")
					for next_object in obj.next_list:
						
						nextstates.append(next_object)
			start = list()			
			seen2 = {}
			nextstates = [seen2.setdefault(x, x) for x in nextstates if x not in seen2]
			starts = list(nextstates)
			nextstates = list()

def mapfunc():
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	nextstates = []
	for step in range(0,steps):
		for start in starts:
			for obj in object_list:
				if ("%s" % obj.name) == ("%s" % start):
					print ("step %s: %s" % (step, start))
					
					for next_object in obj.next_list:
						
						nextstates.append(next_object)
		start = list()				
		starts = list(nextstates)
		nextstates = list()
	
	
def statefunc():
	global object_list
	for obj in object_list:
		print("%s" % obj.name)	



def new(name, tipoint, operator, next_list, cont_list, spec_list):
	global object_list
	name = name.replace(' ', '')
	statement = Statement(name, tipoint, operator, next_list, cont_list, spec_list)
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
	nexts = []
	conts = []
	for serie in series:
		arrowobjs = serie.split('->')
		count = 0
		nexts = list()
		conts = list()
		specs = list()
		tipoint = int()
		operator = str()
		# many nexts vs one
		scale = list()
		for anobj in arrowobjs:
			try:
				eqobjs = arrowobjs.split('=')
				scale = assasement(eqobjs)
				tipoint = scale[1]
				# delete first two and last two characters in scale[1] by [2:-2]:
				conts = split.scale[2][2:-2]
				
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
			new(anobj,tipoint, operator,nexts,conts, specs)			
	seen = {}
	object_list = [seen.setdefault(x.name, x) for x in object_list if x.name not in seen]
	for serie in series:
		arrowobj = serie.split('->')
		count = 0
		nexts = list()
		conts = list()
		# many nexts vs one
		for anobj in arrowobj:
			anobj.replace(" ","")
			if not anobj == "":
				for bnobj in object_list:
					#critical:
					if (" %s " % bnobj.name) == ("%s" % anobj):
						try:
							nexting = arrowobj[count+1].replace(" ","")
							if not nexting == "":
								nexts.append(nexting)
						except:
							pass
						bnobj.next_list += nexts
				count += 1
			count = 0
	#seen = {}
	#object_list = [seen.setdefault(x.name, x) for x in object_list if x.name not in seen]			

	if modeexe == True:
		exefunc()	
	if modeexe == True:
		showfunc()
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
			print ("-h for help\n-f file")
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
