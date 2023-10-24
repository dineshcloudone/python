'''
1.difference() : it only prints/returns the output after difference
2.difference_update() : it will update the first set with the output
3.intersection()
4.intersection_update()
5.isdisjoint() : to check if atleasy one element is matching in two sets, if matches atleast one element it will return True
6.symmetric_difference() : it will print all the elements from two sets which are not matching
7.symmetric_difference_update()
8.issubset()
9.issuperset()
'''

# symmetric difference
set1={1,2,3,4,9}
set2={5,6,7,8,9}
print(set1.symmetric_difference(set2)) #it will print all the elements from two sets which are not matching
