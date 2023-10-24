"""
Installation : pip3 install multipledispatch

By using multipledispatch module we can implement python overloading
"""
#from multipledispatch import dispatch 

class A:
    #@multipledispatch.dispatch(int,int)
    def add(self,a,b):
        return a+b
    
    #@multipledispatch.dispatch(int,int,int)
    def add(self,a,b,c):
        return a+b+c
    
    # @multipledispatch.dispatch(str,str)
    # def add(self,a,b):
    #     return a+b
    
    
obj=A()
print(obj.add(1,2)) # without multiple dispatch will get TypeError: add() missing 1 required positional argument: 'c'
#print(obj.add('learn','python'))
