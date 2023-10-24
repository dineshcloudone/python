'''
keys() - to get all keys
values() - to get all values
items() - to get all items
setdefault() - this method is used to insert item in a dictionary
get() - to get value of given key
'''

k={2:1,'two':1,3:4}

#getting all keys
print('\n getting all keys')
print(k.keys())
print(list(k)) #getting all keys into list
print(set(k)) #getting all keys into set
print(tuple(k)) #getting all keys into tuple

#getting all values
print('\n getting all values')
print(k.values())

#getting all items
print('\n getting all items')
print(k.items())

# to get value of given key
print(k.get(2))
print(k.get(1000)) # if you try to get key which is not there it will give error in this approach
#print(k[1000]) # if you try to get key which is not there it will not give error in this approach

# setdefault
print(k.setdefault(9,9))
print(k.setdefault(9,99)) # with this approach you can't update the values

print(k) 
k['test_key']='test_value' # with this approach you can update the values
print(k)