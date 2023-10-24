"""
In this python array introduction video, i explained 
what is an array?
why we need array data structure in python?
why an array is a homogenous data structure? --> It stores only same data type
why an array is a compound data structure? --> we can add, update, delete array elements
why an array is a mutable data structure? --> at a time we can save more elements
why an array is a sequence data structure? --> it saves elements in sequence memory locations
why an array is a numeric data structure? --> it stores numbers, unicode characters but prefers numbers only
advantages of an array data structure? --> store multiple elements, store single datatype in array, mathematical operations, mutable feature
declaration of array in python?

Array : homogenous datastructure, it works only on unicode characters. Unicode characters mean single letter strings.

An array is homogenous, Mutable, sequence, compound, data structure

Syntax :
array.array(datatype or typecode, listofvalues)
"""

import array 
#array.typecodes

a1_int=array.array('i',[1,2,3,4])
print(a1_int)

a2_float=array.array('f',[1.1,2,2])
print(a2_float)
