# Multiple Inheritance was explained so well in the link below , channel is code basics
# https://www.youtube.com/watch?v=ttMX3Ns_0oY

#git link : https://github.com/codebasics/py/blob/master/Basics/Exercise/18_multiple_inheritance/18_multiple_inheritance.md

class Parent:
   def func1(self):
        print("this is function 1")
class Parent2:
   def func1(self):
        print("this is function 1 in parent2")
class Child(Parent , Parent2):
    def func3(self):
        Parent.func1(self)
        Parent2.func1(self)
        print("this is function 3")
 
ob = Child()
ob.func1()
#ob.func2()
ob.func3()