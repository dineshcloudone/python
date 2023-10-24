# lambda function is anonymous function, 
# lambda function will be mainly used in map, filter, reduce built in functions also in 
# list comprehension,tuple comprehension, built-in functions
#
# Syntax: lambda parameters: expression
#
#
# def function( parameters ):
#    return expression
#
#
# To call lambda function
#
# (lambda parameters: expression)(arguments)


# def squaringNumber(number):
#     return number ** 2

# print(squaringNumber(10))


# print((lambda x:x**2)(9))


# using if else in lambda function

def isEven(number):
    if number%2 == 0:
        print("Even")
    else:
        print("Odd")
        
isEven(14)


(lambda number:print("Even") if number%2==0 else print("Not Even"))(15)

#never store lambda function in a variable and use like below

f = lambda a:a*4
print(f(2))
