"""
Deletion :
1. pop()
2. remove()
3. clear()

Updation :
1.listname[index]
2.listname[start:stop:step]
"""

#Deletion
a=[1,2,3,4,5]
a.pop()
print(a)
a.remove(4)
print(a)
a.clear()
print(a)

#updating, only in sequnce can be updated
b=['a','b','c','d']
b[3]='z'
print(b)
b[-1]=2
print(b)

b[2:5]=[1,2,3]
print(b)

