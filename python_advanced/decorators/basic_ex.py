## Basic Idea behind decorators

def mydecorator(function):
    
    def wrapper(*args,**kwargs):
        value=function(*args,**kwargs)        
        print("I am decorating your function")        
        return value
    return wrapper

@mydecorator
def hello(person):
    #print(f"Hello {person} !")
    return f"Hello {person} !"


print(hello("python"))


################### Basic Idea Explanation (below implementation handles with @mydecorator) ##########################

# func = mydecorator(hello_world)
# func()

### OR ###

#mydecorator(hello_world)()