"""
Lists are mutable : we can insert , update, delete elements in list

Insert Operations :
append() method
insert() method
extend() methos
"""
#append() method
a=['java','python','c']
a.append('hello')
a.append(['a','b'])

print(a)


#insert() method
b=[1,2,3,4]
b.insert(2,5) #inserts 5 at 2nd index
print(b)
b.insert(-2,20)
print(b) #inserts 20 before 2nd position


#extend() methos
c=[1,2,3,4]
c.extend([5])
print(c)
c.extend([1,2,3])
print(c)

