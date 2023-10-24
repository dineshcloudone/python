"""
Method Overriding : Superclass and subclass has same method. If we access the method in subclass then only subclass method is 
accessed without accessing superclass method.


Rules for method overriding :
1. Super class & subclass must be present (Inheritance must be there between two classes)
2. Declare two classes with same method & same parameters
3. Logic must be different in two methods.
4. Method overriding will happen if we access the same method in subclass but not in super class
"""

# ############### Explaining with basic example
# ###############

# class GrandParent:
#     def method(self):
#         print("Grandparent method")
        
# class Parent(GrandParent):
#     def method(self):
#         print("Parent method")

# class Child(Parent):
#     def method(self):
#         print("Child method")
        
# child=Child()
# child.method()
# parent=Parent()
# parent.method()

# Parent.method(None) ## to access parent method


############### Overriding with multiple inheritance

# class Parent1:
#     def method(self):
#         print('This is parent1 method')

# class Parent2:
#     def method(self):
#         print('This is parent2 method')
        
# class Child(Parent1,Parent2):
#     # def method(self):
#     #     print('this is child method')
#     pass
        
# child=Child()
# child.method()
# print(Child.__mro__)


################# Calling parent __init__ in child class

class Parent:
    def __init__(self) -> None:
        print('This is parent constructor method')
    
class Child(Parent):
    def __init__(self) -> None:
        Parent.__init__(self)
        #super().__init__() # here self should not be given as super() method will pass another self
        print('This is child constructor method')
    def test(self):
        self.__init__()
        
ch=Child()
ch.test()

############### When overriding is there how to call parent class method

# class Parent:
#     def method(self) -> None:
#         print('This is parent method')
    
# class Child(Parent):
#     def method(self) -> None:
        
#         """
#         1st way :
#         parentClassName.method(self,arguments)
#         """
        
#         #Parent.method(self)
        
        
#         """
#         2nd way :
#         super.methodName(self,arguments)
#         """
#         super().method()
        
#         print('This is child method')
        


# c=Child()
# c.method()


################ After explaining above programs real time example Mobiles were taken and explained for Iphone, Samsung,realme