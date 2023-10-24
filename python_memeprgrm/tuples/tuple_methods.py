'''
tuple contains only two methods
1. count()
2. index()
'''
a=(1,2,3,4,1,2,9)
print(a.count(1)) #counts the occurance of 1
print(a.count(23)) #output: 0, as given value dont exist

# syntax : tuple.index(element,start,stop)
print(a.index(2)) #prints the index of given number 2

print(a.index(99)) #output : It gives error as given value doesn't exist

