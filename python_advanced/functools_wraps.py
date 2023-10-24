
# functools yoututbe link : https://www.youtube.com/watch?v=Jztj_yuFTlk 

from functools import wraps

def my_decorator(f):
    #@wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')
    #return a + b

func_obj=example()

print(func_obj.__doc__)

#print(func.__name__)
#print(func.__doc__)

# def test1():
#     print("in test1")
#     def test_inner():
#         print("inner test")
#     return test_inner    

# a=test1()
# a()

