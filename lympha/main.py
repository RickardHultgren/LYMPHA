#!/usr/bin/python3
# -*- coding: ascii -*-

class Factor:
	def __init__(self, name, tipoint, operator, next_list, spec_list, cont_list):
        		
		#list of next nodes:
		#next_list = next_list
		next_list = []
		
		#list of specifications:
		#spec_list = spec_list
		spec_list = []

		#list of contents:
		cont_list = cont_list
		cont_list = []

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
		next_list = []
		
		#list of specifications:
		#spec_list = spec_list
		spec_list = []

		#list of contents:
		#cont_list = cont_list
		cont_list = []

		#name
		self.name = name
		
def test():

    pass

if __name__=='__main__':
    test()
