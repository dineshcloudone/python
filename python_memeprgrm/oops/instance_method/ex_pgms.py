"""
3 types of methods

1. Instance method
2. class method
3. static method

In this ,we will explore instance method

Instance method : Methods created inside class are called as instance methods
 -> Instance methods create/access/modify/delete the object attributes
 
 Important : Creating instance method from outside
"""


# #### Creating instance methods
# ####
# class Employee:
#     def instanceMethod1(self):
#         print('instance method 1')
#     def instanceMethod2(self,a,b):
#         print('instance method 2 : ', a , b)


# emp1=Employee()
# emp1.instanceMethod1()
# emp1.instanceMethod2(10,20)


###### Creating instance variables using instance method
######

from types import MethodType


class Employee:
    
    ## to access class variable
    A=10
    
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
        
    ##how to access variables in instance methods        
    def getEmployeeName(self):
        print(self.name)
        
    def getClassVariable(self):
        print(self.A)
        
    ## updating varaible using instance methods
    def updateEmployeeName(self,newName):
        self.name=newName
        
    ## to update class variable inside a method
    def updateClassVariable(self,newName):
        self.__class__.A=newName
        
    ## deleting instance variable using instance method
    def deleteInstanceVariable(self):
        del self.name
        
    ## deleting class variable using instance method
    def deleteClassVaraible(self):
        del self.__class__.A

emp1 = Employee('pavan',1,70000)

# print('emp_name:',emp1.name)
# print('emp id:',emp1.emp_id)
# print('emp sal:',emp1.salary)

# emp1.getEmployeeName()

# emp1.getClassVariable()

# emp1.updateEmployeeName('New Name')
# print(emp1.name)

# emp1.updateClassVariable('New Name')
# print(emp1.A)

# emp1.deleteInstanceVariable()
# print(emp1.name) # Gives attribute Error

# emp1.deleteClassVaraible()
# print(emp1.A) #gives attribute Error 

### Creating instance method from outside the class and adding it to class

"""
Syntax :

object.methodName=MehodType(function,object)

"""

def addMethod(self):
    print("method added successfully from outside")

## to whatever object we are adding new method only that object can call this method
emp1.newInstanceMethod=MethodType(addMethod,emp1)
emp1.newInstanceMethod()