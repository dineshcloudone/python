import array

a1=array.array('i',[1,2,3,4,5,6,7,8,9])

"""
syntax : variableName[start:stop:step]

default value for start = 0
default value for stop = length of array
default value for step = 1

ex: if we give stop value as 7, it will print upto index 6

slicing : 

subarray [5,6,7,8]

start = 4th index 
stop = subarray first index - subarray  second index (5-4 =1)
step = 1

Postive step value -> it is farward direction

Negative step value -> it is reverse direction

"""

print(a1[1:4:1]) #default start value is 0 and step value is 1
#output : array('i', [1, 2, 3, 4])

print(a1[1:-4:])
#output : array('i', [2, 3, 4, 5])

print(a1[-1:-4:-1])
#output : array('i', [9, 8, 7])

print(a1[-6:-10:-1])
#output : array('i', [4,3,2,1])

print(a1[-8:-3:2])
#output : array('i',[2,4,6])

print(a1[-1:-8:-3])