import re

filename = "test.lympha"

textfile = open(filename, 'r')

filetext = textfile.read()

filetext = filetext.replace('\n', ' ')

filetext = filetext.replace('  ', ' ')

series = []
series = filetext.split(';')


print (series)

states = [] 
substates = []
nextstates = []
specs = []
tipoint = None
operator = None

'''
		#name
		self.name = name
		
		#tipping point
		self.tipoint = tipoint
		
		#relational operator
		self.operator = operator
'''
