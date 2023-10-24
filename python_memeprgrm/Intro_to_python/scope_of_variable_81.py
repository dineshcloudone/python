'''
global scope
enclosed scope
local scope

Built in scope : using a variable any where without any declaration. It will be in a case where we import a built in moudle or function
'''

a=10 # global scope
def func_1():
    b=20 # envclosed scope
    
    def func_2():
        c=30 # local scope
        print(a)
        print(b)
        print(c)

print(a)
print(b) # error
print(c) # error