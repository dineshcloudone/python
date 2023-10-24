'''
filter() - pre defined function in python
it will check the given condition for every element in an iterable

syntax : 
    filter(function,iterable)
    
    iterbale :  list,tuple,set,dict,string,array,range,...etc
    
    Function : Normal Functions, Built in functions, Lambda functions
    
filter function don't store : False,None,'',0,[],{},() in filter object
'''

a=[1,2,3,4,5,6,7]

def func(i):
    if i%2==0:
        return True
    
result = filter(func,a) # it returns a generator object of filter function
print(list(result)) # converting generator to list, output : [2, 4, 6]

## Implementing above logic using lambda function

result2 = filter(lambda i:i%2==0,a)
print(list(result2))


## other example

alpha = 'abcdefghijklmnop'

def func2(i):
    if i not in 'aeiou':
        return True
result3=filter(func2,alpha)
print(list(result3))