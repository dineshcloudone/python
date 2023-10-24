'''
o Set is built in data structure

o We use Set when we don't want to store duplicate values in a set and set will not store data in organized order
  And because it doesn't store data in sequence order , we can't use indexing and slicing.

o Set is heterogenous compound collection mutable data structure.

o Set stores only immutable data types, it means it will not support List, dictionary and array because these are mutable datatypes

o Set is mutable, so it can be altered after creation.

o Collection data structures are two types:

    1. Set
    2. Dictionary

Set syntax : {value1,value2,value3....}

'''

# to declare empty set use - set() not {} because curly braces represent dictionary
d=set()
print(type(d)) # <class 'set'>

a={1,2,3,4,5,6,7,8,9}
print(a)

b={'a','b','c','a','b','c','e','f'}
print(b)

c={1,'a',2,'b',3} # Heterogenous datatype can store different data types at a time in single datatype.
print(c)


