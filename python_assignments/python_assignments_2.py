# Write a python script to add comments and print “Learning Python” on screen.
from keyword import kwlist
import plistlib


print("Learning Python")

## Write a python script to add multi line comments and print values of four variables,
## each in a new line. Variable contains any values.
"""
this is muiltiline comment
"""
a=1
b=2
c=3
print(a)
print(b)
print(c)
#================================================================================
#Write a python script to print types of variables. Create 5 variables each of them
#containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
 
a=35
b=True
c="MySirG"
d=3+4j
print(a,b,c,d)

#print the id of two variables containing the same integer values.
a=1
b=1
print(id(a),id(b))

# print value, its type and id of each variable
aa=35
bb=True
cc="MySirG"
dd=3+4j
print (type(aa),type(bb),type(cc),type(dd))
print (id(aa),id(bb),id(cc),id(dd))
# print keywords
print(kwlist.keywords)