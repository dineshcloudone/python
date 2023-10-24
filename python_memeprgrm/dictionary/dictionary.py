'''

Dictionary is heterogenous compound collection mutable data structure.

We can store any datatype in dictionary like int, float, tuple, list, set, etc... so it is heterogenous datatype

key supports ony immutable datatype

key doesn't support duplicate values and if we give duplicate value it will take latest value

Syntax :
{key1:value1,key2:value2,key3:value3,....keyN:ValueN}

'''

# declaring empty dictionary
a=dict() # or a={}
b={}
print(type(a))
print(type(b))

sample1={'a':1,'b':2,'c':3}
sample2={'key1':1,'key2':2,'key3':3}

sample3={'a':1,2:'b',(1,2):23}

print(sample1,sample2,sample3)

#sample4={[1]:2,'b':3} #output : gives error unhashable type:'list'


# key doesn't support duplicate value

sample5={'a':1,'a':2,'b':3}

print('sample5 : {}'.format(sample5)) #output : sample5 : {'a': 2, 'b': 3}
