import array

a1=array.array('i',[1,2,3,4,5,6,7,8,9])


# a1.append(2) #to add a value at the end of array
# print(a1)

# a1.insert(3,10) # to insert value at given index
# print(a1)

# a1.insert(50,10) # even if we give index out of range it will the element at the end of the array
# print(a1)

# a1.insert(-2,33) # insert can be done using negative index also
# print(a1)

# a1.extend([22,33,44]) # to add more than one element, here we have given list
# print(a1)

# a1.extend((-1,-2,-3))
# print(a1)

# a1.fromlist([1,2,3]) #to add elements from only list
# print(a1)

a1.pop(3) #deletion method , it will delete the element based on given index
print(a1)

a1.remove(9) #it removes given element
print(a1)

a1[2] = 222 # inserts 222 value at index 2, we can also give negative index
print(a1)

#other mehtods
"""
reverse() -> a1.reverse()
count() -> a1.count(element)
index() -> a1.index(element)
tolist() -> a1.tolist()

"""

a1.reverse()
print(a1)

for i in a1:
    print(i, end =' ')
print()

print("count:"+str(a1.count(2)))
print("index :"+str(a1.index(1)))
print("tolist:"+str(a1.tolist()))

print(id(a1))
print(type(a1))