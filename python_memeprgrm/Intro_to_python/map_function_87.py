"""

Syntax :

map(function,iterable) : here each element of iterable will be passed to function and map will return its object
Iterable - list,tuple,set,dict,string,array,range ...etc
function : normal functions , built in functions, lambda functions

"""

import math

sample_list=[1,2,3,4,5]

def square(i):
    return i**2
print(square(2))


result=map(square,sample_list)
print(list(result))


result2=map(lambda i:i**2,sample_list)
print(result2)

result3=map(str,sample_list)
print(list(result3))

sample_list_2=[2.567,8.9,9.1]
print(list(map(math.floor,sample_list_2)))


"""
Program : Given tuple of values 
if element is Even then square the number
if element is Odd then cube the number
"""

sample_tuple=(1,2,3,4,5)

def squareCube(i):
    if i%2==0:
        return i**2
    else:
        return i**3

sq_cub_result=map(squareCube,sample_tuple)
print(list(sq_cub_result))


#with lambda function
lamb_sqcub_result=map(lambda i:i**2 if i%2==0 else i**3,sample_tuple)
print(list(lamb_sqcub_result))

#using map converting given input into list/set/tuple
inputList=list(map(int,input().split()))
print(inputList)
