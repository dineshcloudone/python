'''
What is a tuple ?
How to declare a tuple ?
Is tuple COMPOUND DATATYPE, HETEROGENOUS DATATYPE, SEQUENCE DATATYPE, why ?
tuple is immutable datatype ?
how to access elements from a tuple ? #using index
how to access using negative index ? #using negative index


tuple : it is one the memory efficient heterogenous immutable sequence compound data structure
        we will tuple to store data and do not want to change the data again.
        to have datastructure fixed size (ex : latitude, longitude)

syntax :
(value1, value2,....,valueN)

'''

sampleTuple=(1,2,3,4,5)
print(sampleTuple)
print(type(sampleTuple))

#creating empty tuple
tuple1=tuple()
tuple2=()

#heterogenous datatype
a=(1,'abc','9.9',True)
print(a)

#tuple is immutable, here you have no methods to modify tuple
b=(1,'abc')
print(b.count(1))
print(b.index(1))