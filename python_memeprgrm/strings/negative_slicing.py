"""
a    b   c  d  e  f  g  h  i  j  k
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
0    1   2  3  4  5  6  7  8  9  10


if we have to give 0 for stating index or length of string in end index or step value as 1 
in the above cases we can leave those fields

a[:] # prints total string

string reverse : s[::-1]
also need to know using negative step value

"""

s='abcdefghijk'
print(s[-11:-7]) #output : abcd


# if there is one positive and one negative in slicing, convert both to one type either positive or negative
print(s[:-7]) #output : abcd

#converting to positive
print(s[0:4])

# or coverting to negative
print(s[-11:-7])

print(s[::-2]) # output : kigeca