"""
Methods :
--------

1. replace()
2. count()
3. isspace()
4. startswith()
5. endswith()
6. isidentifier()
7. isalpha()
8. isdecimal()
9. isdigit()
10. isnumeric()
11. isalnum() 

"""


"""
string.replace(old,new,count) #count is option and default value is -1
"""
a='d3v3lopm3nt'
print(a.replace('3','e'))


"""
string.count(element,start,end) #start and end are optional
"""
d='potato'
print(d.count('o'))



"""
string.isspace()
"""
print('---is_space---')
print(' '.isspace())
print('j '.isspace())


"""
string.isidentifier(parameter) 

True if the string is in identifier format. other wise False

Rules : 
    1. identifier cannot start with numbers
    2. identifier cannot contain special chars apart from underscore
"""
print('meme7'.isidentifier()) #output: True , becuase we can use meme7 as identifier



"""
string.isalpha()

True if string contains only alphabets else False
"""

"""
string.isdecimal()

True if string contains only decimal[0-9] numbers. otherwise False
"""
print('123.456'.isdecimal()) #output : false

"""
string.isdigit()

True if string contains only decimal [0-9]. otherwise False
The decimals are in base, superscript,subscript
"""
# time in video : 11:00
#print('123')- not sure how to get superscrpt and subcript need to google it

"""
string.isnumeric()

True if string contains decimals (the numbers are in superscript, subscript), roman numerals, fractional numbers
    otherwise False
"""
#print('IV123'.isnumeric()) - not sure how to give roman num, fractions


"""
string.isalnumeric()

True if string contains decimals (the numbers are in superscript, subscript), roman numerals, fractional numbers, alphabets
    otherwise False
    
isalpha() + isnumeric() = isalnumeric()
"""