"""
Abstraction : 
1. The process of handling complexity by hiding unnecessary information from user is called abstraction.
2. We can use Abstract classes for implementing Abstraction.
3. Abstract classes will be used as blueprint for other classes. these will be used at design level

Abstraction
    vs
DataHiding
    vs
Encapsulation
    vs
Message parsing

If a class contains one or more than one abstract method then the class is called abstract class.

If the method is declared without implementation it is called abstract method.

Abstract classes used as blueprint for another class : 
    1. If a project has lot of classed & functions then developers create abstract class & use the classes by inheriting.
    2. If we have to define set of classes if the classes have common behavior then we create abstract classes & derive into 
        child classes

"""

from abc import ABC, abstractmethod

# #abstract class creation
# class A(ABC):
#     @abstractmethod
#     def method1(self):
#         pass
#     def method2(self):
#         print('this is a concrete method')
#     @abstractmethod
#     def method3(self):
#         pass
#     @abstractmethod
#     def method4(self):
#         pass

# # obj=A()
# # obj.method1() #Error : Cannot instantiate abstract class A with abstract method method

# #child class to import abstract class
# class B(A):
#     def method1(self):
#         print('Method1 is implemented in subclass')
#     def method3(self):
#         print('Method3 is implmented in subclass')
        
# obj1=B()
# obj1.method1()
# obj1.method2()
# obj1.method3()



############### Polygon example
###############
"""
Triangle  - 3 sides
Rectangle - 4 sides 
Pentagon - 5 sides
hexagon - 6 sides
octagon - 8 sides
"""
from abc import ABC, abstractmethod
from math import sqrt

class Polygon(ABC):
    
    @abstractmethod
    def sides(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    
    def figure(self):
        return "It is a two dimensional plane figure"
    

class Rectangle(Polygon):
    
    def sides(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
    def extramethod(self):
        return 'rectangle has 4 sides'
    
class Triangle(Polygon):
    
    def sides(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s=self.perimeter()
        return sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
    def perimeter(self):
        return (self.a+self.b+self.c)/2
    
    def extramethod(self):
        return 'triangle has 3 sides' 
    

class Square(Polygon):
    
    def sides(self,side):
        self.side=side
        
    def area(self):
        return self.side*self.side
    
    def perimeter(self):
        return 4*(self.side)
    
    def extramethod(self):
        return 'square has 4 sides' 
    
    
rect = Rectangle()
rect.sides(10,20)

tri=Triangle()
tri.sides(10,20,30)

squa=Square()
squa.sides(10)

for obj in [rect,tri,squa]:
    print(obj.area())
    print(obj.perimeter())
    print(obj.extramethod())
    print(obj.figure())