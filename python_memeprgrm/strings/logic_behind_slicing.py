a='abcdefghij'
"""
condition to print the element
index < end

a b c d e f g h i j
0 1 2 3 4 5 6 7 8 9 

current index = 0
new index = current index + step value
"""
print(a[:5])

# to print only odd numbers in the given string
b='123456789'
print(b[::2]) # output : 13579

# to print only even numbers in the given string
print(b[1::2])

# another exammple
s='12a34b56c78d90e'
print(s[2::3]) #output : abcde