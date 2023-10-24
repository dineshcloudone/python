"""
part 1:
------
capitalize()
title()
istitle()
upper()
isupper()
lower()
islower()
swapcase()
index()
find()
"""

a="abcd efgh"
print(a.capitalize()) #output : Abcd efgh

print(a.title()) #output : Abcd Efgh

print(a.istitle()) #output : False

print(a.upper()) #output : ABCD EFGH

print(a.isupper()) #output : False

print('THIS'.lower()) #output : this

print('this'.islower()) #output : True

print('aBcD'.swapcase()) #output: AbCd


# index() is used to get index of given element and also we can pass search index range for given element
print('potato'.index('o')) #output : 1

print('potato'.index('o',2,6)) #output : 5

# z is not there in the given string
#print('potato'.index('z')) # output : ValueError:Substring not found

b='everything is connected'
print(b.index('is')) #output : 11

#if we dont specify third parameter it will take length of the parameter
print(b.index('is',4)) #output : 11


#find() - the only difference between find() and index() is find() returns -1 if given element is not found
print('find()')
s = 'vivekananda'
print(s.find('n'))
print(s.find('n',7))

print(s.find('z')) #output : -1

"""
Other methods :replace(old,new,count), count(old,new,count), isspace(), startswith(), endswith(), isidentifier(), isalpha()
isdecimal(), isdigit(), isnumeric(), isalnum()


ASCII : 0's and 1's

65-90 (A-Z)
97-122 (a-z)
45-58 (0-9)

Built-in Functions : These methods are not just for strings also used for list,set,tuple,dictionary,string and array
min(), max(), chr(), ord(), sorted(), len()

print(chr(68)) #output : 'D'

print(chr(98)) #output : 'b'

print(ord('p')) #output : 112

print(max('1234')) #output : 4

print(min('1234')) #output : 1

print(len('meme programmers)) #ouput : 16

print(sorted('987654321')) #output : ['1','2','3','4','5','6','7','8','9']
"""

name="this is python programming"

print(name.capitalize())
print(name.title())
print(name.istitle())
print(name.index('p',4,9)) #throws ValueError if given string was not found
print(name.find('p',4,9)) #return -1 if given string was not found
print(name[::-1]) #string reverse