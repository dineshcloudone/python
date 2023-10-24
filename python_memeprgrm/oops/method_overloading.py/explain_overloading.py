"""
Method Overloading : If the class contains more than one method with same name & methods contain different datatypes of parameters 
(or) different no of parameters (or) both is called method overloading.

Features :

1. Flexibility
2. Readability

Python doesn't support method overloading because, Python is dynamically type language (it means datatype will be known at run time)
"""

# ##### Same method with different types of parameter

# class A:
#     def method(int,int):
#         pass
    
#     def method(str,str):
#         pass
    
#     def method(float,float):
#         pass
    
    
# ##### Same method with different no of parameters

# class B:
#     def method(int):
#         pass
    
#     def method(int,int):
#         pass
    
#     def method(int,int,int):
#         pass
    
# ##### Same method with different no of parameters and different datatypes

# class C:
#     def method(int,int):
#         pass
    
#     def method(str,str,str):
#         pass
    
#     def method(float,float,float.float):
#         pass