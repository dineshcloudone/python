'''
Built in fucntions / built in methods : These are same for List, Tuple, Set, String, Array and Dictionary

Ascii video for strings : https://www.youtube.com/watch?v=V-0uBDMpPMc&t=61s

max() - it will work only if there is only data type values in tuple otherwise it will not work (decimal and float can be used)
min() - it will work only if there is only data type values in tuple otherwise it will not work (decimal and float can be used)
len() - to get number of elements 
sorted() - to sort the elements in the tuple
sum() - it should be used only if data is decimal, float, boolean type


Syntax :
    max(iterable)
    iterable - tuple
'''

# max and min functions

a=(1,2.3)
print(min(a))
print(max(a))

# Sum
# a= (True,True,True,False) # True will hole value 1
# print(sum(a))

# b=(1,2,1.3,2.3,True)
# print(sum(b))