'''
add : set.add(element)
pop : removes first value in set - set.pop()
remove : removes any given element in the set - set.remove(element), if we given non existing value throws error
discard : removes any given element in the set - set.discard(element), if we given non existing value then it will not give error
clear : Deletes all elements in the set
copy : to copy elements from one set to another set - variable = set.copy()
union : to join two sets - set1.union(set2)
update : it will update first set (set1) with result - set1.update(set2)

range() is an object which is immutable
'''

# copy
# a= {1,2,3}
# b=a  # using = will assign reference of memory address
# b.add(4)
# print(a)
# print(b)

# c=a.copy() # duplicate set will be copied
# c.add(9)
# print(a)
# print(c)



# Union
# set1={1,2,3,4}
# set2={5,6,7,8}
# set3=set1.union(set2)

# print(set1)
# print(set2)
# print(set3)


#update - it will update result of union to first set used before dot

set1={1,2,3,4}
set2={5,6,7,8}
set1.update(set2)
print(set1)



