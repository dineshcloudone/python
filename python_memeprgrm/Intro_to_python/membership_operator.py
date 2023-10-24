'''
Membership operator : To check whether the given element [value or variable] is present in iterator or not

iterator : list,tupe,set,dictionary,string,range & array

Two membership operators :
in operator
not in operator

o 'in' operator works Fast in Set and Dictionary
'''

'''
>>> 2 in [1,2,3,5]
True
>>> 1 in [4,5,6,7]
False
>>> a in 'apple'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'in <string>' requires string as left operand, not list
>>> 'a' in 'apple'
True
>>> 2 in (1,2)
True
>>> 9 in range(10)
True
>>> 10 in {1,2,40}
False
>>> 'a' in {1:2,2:4,'a':4}
True
>>> 

>>> 'a' not in 'apple'
False
>>> 'e' not in 'meme'
False

>>> 2 not in (1,4,5)
True
>>> 

>>> 9 not in range(4)
True
>>> 

'''