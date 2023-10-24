"""
Static Method (like utility method): These are general methods, used to do general tasks
1. Static method doesn't perform operations on class variables and instance variables

we can access instance methods using only objects
we can access class methods using Both class & objects
Static Methods also can be accessed using class and objects
"""
### Calculator App
###

class Calculator:
    
    @staticmethod #it is decorator
    def add(a,b):
        return a+b
    
    @staticmethod #it is decorator
    def sub(a,b):
        return a-b
    
    @staticmethod #it is decorator
    def mul(a,b):
        return a*b
    
    @staticmethod #it is decorator
    def div(a,b):
        return a/b
    
print('accessing static methods using class name')
print(Calculator.add(9,9))
print(Calculator.sub(9,8))
print(Calculator.mul(3,3))
print(Calculator.div(9,3))

print('accessing static methods using object')

cal1=Calculator()
print(cal1.add(1,2))
print(cal1.sub(4,2))
print(cal1.mul(9,8))
print(cal1.div(9,3))


    
    

