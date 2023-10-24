"""
1. class
2. object
3. Inheritance
4. polymorphism
5. encapsulation
6. abstraction

class - Blue print for object creation.
object - instance of a class

we follow pascal naming convention
we follow indentation which is 4 white spaces
"""

class SampleClass:
    attribute1=10
    attribute2=20
    
print(SampleClass.attribute1)
print(SampleClass.attribute2)

########### OR

obj1=SampleClass()
obj2=SampleClass()

print(obj1.attribute1)
print(obj1.attribute2)
print(obj2.attribute1)
print(obj2.attribute2)

# print("######## changing attribute value")
# obj1.attribute1=100
# print(obj1.attribute1)
# print(obj2.attribute1) #in obj2 attribute1 will not be changed
# print(SampleClass.attribute1) #class attributes also will not be changed by objects


print("############ changing attribute value by obj1 and also with class")
obj1.attribute1=100 # it creates a separate attribute1 for obj1 no relation with class attribute1
SampleClass.attribute1=1
print(obj1.attribute1)
print(obj2.attribute1)