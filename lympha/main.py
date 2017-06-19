#!/usr/bin/python3
# -*- coding: ascii -*-

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

def exe():
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
	new("hypovolemia",None,None)
	new("hypervolemia",None,None)
	for obj in object_list:
		obj.next_list = ["abc"]
		print (obj.next_list)
		print("%s" % obj.name)	
	
if __name__=='__main__':
    run()
