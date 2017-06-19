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




object_list.append(Event(i))
object_list.append(Factor(i))

def exe():
	for next_object in next_list:
		for list_object in object_list:
			if list_object == next_object:
				exe_objects.append(list_object)
	for exeobject in exe_objects:
		if exeobject.flow==1 :
			execute exeobject
			for subexeobject in exeobject.subobjects
				execute subexeobject
			#pointer to list-object is added to PAST-LIST-OF-OBJECTS-TO- EXECUTE
			#delete exeboject-pointer in LIST-OF-OBJECTS-TO-EXECUTE
	for pastexeobject in PAST-LIST-OF-OBJECTS-TO-EXECUTE:
			EXECUTE FUNCITON (pastexeobect.next)
		
def test():

    pass

if __name__=='__main__':
    test()
