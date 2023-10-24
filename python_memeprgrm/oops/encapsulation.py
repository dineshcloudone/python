"""
Encapsulation : Combining related things into a single unit


    Data & Method ---> accessed using object ---> it relys on class

Advantages :
1. Code will be organized and clean
2. Prevents the data from accidental removal & deletion
Ex : Pandas library can be used in the form of classed but we cannot modify it
3. Abstraction : Hides implementation logic and allows only to use
4. Datahiding : using access modifiers to hide data
5. Modularity (defining classes)

Datahiding + Abstraction = Encapsulation

3 types of access specifiers (below explanation is for java)

In python private, protected data is accessed same as public data 

1. public
    can be accessed : in same class, by same class object, can be accessed from subclass & subclass object
2. private
    can be accessed : only in that class
3. protected
    can be accessed : only in that class and derived class


Name Mangling : Declare data or method with atleast 2 leading underscores and atmost 1 trailing underscore. Then it will replace
to _className by the interpreter

  ex : _ _ data _
  
  print(dir(ClassName)) --> helps to know mangling, it will return all variable and methods

"""

######## Example for public access specifier

# class Parent:
#     publicData = 10
#     def publicMethod(self):
#         print(self.publicData)

# class Child(Parent):
#     def method(self):
#         print(self.publicData)
        
        
# obj1 = Parent()
# obj1.publicMethod()
# print(obj1.publicData)

# obj2=Child()
# obj2.method()
# print(obj2.publicData)


##### Example for protected access specifier


# class Parent:
#     _protectedData = 10
#     def publicMethod(self):
#         print(self._protectedData)

# class Child(Parent):
#     def method(self):
#         print(self._protectedData)
        
        
# obj1 = Parent()
# obj1.publicMethod()
# print(obj1._protectedData)

# obj2=Child()
# obj2.method()
# print(obj2._protectedData)


###### Example program for private access specifier
class Parent:
    __privateData = 10
    def publicMethod(self):
        print(self.__privateData)
        
        
class Child(Parent):
    def method(self):
        print(self._Parent__privateData)

obj1=Parent()
obj1.publicMethod()
obj2=Child()
obj2.method() #  (without name mangling) :  Attribtue error 'Child' object has no attribute '_Child__privateData'
print(obj2._Parent__privateData) #Name

