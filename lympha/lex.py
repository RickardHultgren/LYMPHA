import re

filename = test.lympha

textfile = open(filename, 'r')
filetext = textfile.read()
textfile.close()

#variable name ( specification) = content
spec = r'(\w*[a-zA-Z]\w*\.)\(^[^\)]*?(?=\))?\s*?=\s*?(^[^ ;]*?(?=;))'
list1=re.findall(statement,filetext)


#datatype [ sub-variable name ] = content
cont = r'(\w*[a-zA-Z]\w*\)\[^[^\]]*?(?=\])?\s*?=\s*?(\w*[a-zA-Z]\w*\)'
list1=re.findall(statement,filetext)

#{ event , factor , event }
[x.strip() for x in content.split(',')]

#tipping point   relational operator | {  sub-factor , sub-factor} |
tipoint = r'\regex{(\d)\s*?(==|>|<|>=|<=)\s*?\{(\w*[a-zA-Z]\w*\)\}}'
list1=re.findall(statement,filetext)

