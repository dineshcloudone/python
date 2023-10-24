"""
Generally any method created in class we call it as instance method and these are used to make operations on instance variables

Class Method : To perform operations on class variables and also to handle factory methods
 1. We cannot access instance variables using class methods
 2. We can access class variables using objects & using class
 
 We may think like when we are able to do operations on class variables using object why we need class methods, 
 so to explain this we can here we are not using class methods only for accessing class variable but also to handle factory methods
"""

#### Creating class method
"""
Syntax : 

@classmethod:
def methodName(cls,parameters):
    Body
"""

# class Student:
    
#     college='xyz'
    
#     @classmethod
#     def classMethod(cls):
#         print('class method created successfully')
    
#     @classmethod
#     def classMethod2(cls):
#         print(cls.college)
        
#     @classmethod
#     def classMethod3(cls,new_value):
#         print(cls.college)
#         cls.college=new_value
#         print('updated value',cls.college)
    
    
#     @classmethod
#     def classMethod4(cls):
#         del cls.college
#         print(cls.college)
            
# """ Syntax to call class method
# object/className.classmethod(arguments)
# """

# Student.classMethod()

# ##Accessing class method using object
# student1 = Student()
# student1.classMethod()

# ##now we will see accessing class variable
# Student.classMethod2()

# ##updating class variable using class method
# Student.classMethod3('ABC')


##### Factory methods are used to create object using method
##### Factory method works as alternate constructor

import datetime

class Student:
    
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
    
    @classmethod
    def getAgeAsDOB(cls,name,id,age):
        return cls(name,id,datetime.datetime.now().year-age)
    
std1=Student.getAgeAsDOB('Abcd',1,20)
print(std1.name,std1.id,std1.age)

std2=Student('sdcd',2,30)
# std3=Student('kmcd',3,40)

print(std2.name,std2.id,std2.age)