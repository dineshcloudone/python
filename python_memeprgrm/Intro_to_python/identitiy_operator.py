'''
Identity operators used to check the object reference is same or not.

Everything is object in python

id() : function is used to find the object reference.

Identity operator are two types : 

1. is identity operator : Retrurns True if two object references match and False if not matches
2. is not identity operator

if object reference is same then values are automatically same

Object is :
integer object,
string object,
set object,
list object,
class object,
function object,
boolean object.. etc.

'''


'''

root@dinesh1:~# python3
Python 3.7.17 (default, Jun  6 2023, 20:10:10) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a=[1,2]
>>> b=[1,2]
>>> a is b
False
>>> id(a)
140364545500656
>>> id(b)
140364545549728
>>> c=10
>>> d=10
>>> c id d
  File "<stdin>", line 1
    c id d
       ^
SyntaxError: invalid syntax
>>> c is d
True
>>> id(c)
9392640
>>> id(d)
9392640
>>> [1] is 1
False
>>> a is not b
True
>>> c is not d
False
>>> [1] is not 1
True
>>> 

'''