"""
3 types of variables

1. static variables or class variable
2. instance variable
3. local variable


Local Variable : Variable which are declared inside method is called local variable (same as variable declaration in function)

Here we will explore static variable or class variable and instance variable

static variable or class variable : if we declare a variable inside class and outside method then it is class variable, 
                                    if all objects has same value then we declare that variable as static variable

we can create,update,access,delete class variable using class name. But we can only access class variable using object.
"""

##################### Class Variable or Static Variable

# class A:
#     #class variable also we can define class variable like "className.variable = value"
#     staticVariable1 =10
#     staticVariable2 =20
    
#     def sampleMethod(self):
#         print("sample Method")
        
#     def method1(self):
#         print(self.staticVariable1)
#         print(A.staticVariable1)
        
# A.staticVariable3 = 30

# """
# accessing static variable in two ways
# 1. className.staticVariableName (using class name)
# 2. obj.staticVariableName (using class obj)

# if we want to access class variable in class method we can use below ways
# 1. className.variableName
# 2. self.variableName


# """
# print("Printing using Class Name")
# print(A.staticVariable1)
# print(A.staticVariable2)
# print(A.staticVariable3)

# obj=A()
# print("Printing using object")
# print(obj.staticVariable1)
# print(obj.staticVariable2)
# print(obj.staticVariable3)

# print("Accessing method using object")
# obj.method1()

# #updating class/static variable with class Name
# A.staticVariable1=90

# print(obj.staticVariable1)

# #Updating class variable with object will not work
# obj.staticVariable1=80

# print("printing class variable staticVaraible1 after updating(as 80) it using object, which will not work")
# print("className.staticVariable1",A.staticVariable1)
# print("obj.staticVariable1",obj.staticVariable1)

# ################# Instance Variable
# #################

# """
# Whenever a variable is created for object then it is instance variable

# we can access instance variable in two ways
# 1. self.variableName = variableName
# 2. obj.variableName = variableName

# we cannot access one object attributes with another object
# """
# class A:
#     def __init__(self,a,b) -> None:
#         self.instanceVariable1=a
#         self.instanceVariable2=b
        
#     def updateVariable(self,newValue):
#         self.instanceVariable1=newValue

# obj=A(10,20)
# obj.instanceVariable3=30
# print(obj.instanceVariable1)
# print(obj.instanceVariable2)
# print(obj.instanceVariable3)


# """
# We cannot access one object attribute with another object
# """
# obj2=A(100,200)
# print(obj2.instanceVariable1,'this is obj2 var1')
# print(obj2.instanceVariable2,'this is obj2 var2')
# #print(obj2.instanceVariable3,'this is obj1 var3') # it will give error

# obj.instanceVariable1=300

# print(obj.instanceVariable1,'instance var1')
# obj.updateVariable(3000)
# print(obj.instanceVariable1,'after updating var1 with method')


############# Real Example
#############

class Student:
    
    schoolName ='XYZ'
    
    def __init__(self,name,rollNo,address,phoneNo):
        self.name=name
        self.rollNo=rollNo
        self.address=address
        self.phoneNo=phoneNo
        #self.schoolName='ABC' #if we have to change it we have to change it for all objects
    
s1=Student('A',1,'a',12334)
s2=Student('B',2,'b',12334)
s3=Student('C',1,'c',12334)

for obj in [s1,s2,s3]:
    print(obj.name)
    print(obj.rollNo)
    print(obj.address)
    print(obj.phoneNo)
    print(obj.schoolName)