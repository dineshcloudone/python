# Inheritance : Inheritance is ability to derive the capabilities(properties and methods) from one class into another class.

"""
Single Inheritance
Multilevel Inheritance
Multiple Inheritance
Hierarchical Inheritance
Hybrid Inheritance
"""

# ######### Single Inheritance



# class Parent:
#     def parent_method(self):
#         print("parent class")
        
# class Child(Parent):
#     def child_method(self):
#         print("child method")
        
# print("####### Single Inheritance")        

# child=Child()
# child.parent_method()
# child.child_method()
# print(Child.__mro__) #(<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)


# ########## Multilevel Inheritance


# class GrandParent:
#     def grandparent_method(self):
#         print("grand parent class")
        
#     def method_test(self):
#         print("this is test method from GrandParent")

# class Parent(GrandParent):
#     def parent_method(self):
#         print("parent class")
        
# class Child(Parent):
#     def child_method(self):
#         print("child method")
        
# print("####### Multilevel Inheritance")        

# child=Child()
# child.parent_method()
# child.child_method()
# child.method_test()
# print(Child.__mro__) # (<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.GrandParent'>, <class 'object'>)


# ############# Multiple Inheritance

# class GrandParent:
#     def parent_method(self):
#         print("grand parent class")

# class Parent:
#     def parent_method(self):
#         print("parent class")
        
# class Child(GrandParent, Parent): #method will be called from GrandParent class as it comes first in the order, we can test interchanging them
#     def child_method(self):
#         print("child method")
        
# print("####### Multiple Inheritance")    

# child=Child()
# child.parent_method()
# print(Child.__mro__)


# ########### Hierarchical Inheritance

# class Parent:
#     def parent_method(self):
#         print("parent class")
        

# class Child1(Parent):
#     def child1_method(self):
#         print("child_1 method")
        
# # class Parent2:
# #     def parent2_method(self):
# #         print("parent2 method")
        
# #class Child2(Parent,Parent2):
# class Child2(Parent):
#     def child2_method(self):
#         print("child_2 method")

# print("####### Hybrid Inheritance")        

# child1=Child1()
# child2=Child2()
# child1.parent_method()
# child2.parent_method()
# print(Child1.__mro__)
# print(Child2.__mro__)

############ Hybrid Inheritance

class Parent1:
    def parent_method(self):
        print("parent1 class")        

class Child1(Parent1):
    def child1_method(self):
        print("child_1 method")
        
class Parent2:
    def parent_method(self):
        print("parent2 method")
        
class Child2(Parent2,Parent1):
#class Child2(Parent):
    def child2_method(self):
        print("child_2 method")

print("####### Hybrid Inheritance")        

child1=Child1()
child2=Child2()
child1.parent_method()
child2.parent_method()
print(Child1.__mro__)
print(Child2.__mro__)



