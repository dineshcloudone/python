
"""
split :
--------
split() : splits the string at given element or substring
syntax :

string.split(element,splitcount)
element : where the string has to be splitted
splitcount : how many times we want to split, default value is -1 and it is optional

"""

a="this is python"
print(a.split('is'))

print('meme programmers youtube channel'.split(' ')) #output : ['meme', 'programmers', 'youtube', 'channel']

print('development'.split('e')) #output : ['d', 'v', 'lopm', 'nt']

#applying split only two time
print('development'.split('e')) #output :

#if there is not element with given value then it will not split
print('python'.split('e')) #output : ['python']


"""
join():
--------

--> join method joins the string with iterators

Compound data types
String
List
set
Tupple
Array
Range
Dictionary
"""

b="hi" # for Range and Array this join method will not support

#in the below example 1234 is called iterator
print(b.join('1234'))
