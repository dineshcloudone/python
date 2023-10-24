"""
What is Polymorphism: The word polymorphism means having many forms. In programming, 
polymorphism means the same function name (but different signatures) being used for different types.

Operator Overloading : 

    ex: Plus('+') - It concatenates two strings, lists and also add two numbers
        Multiplication('*') - Multiplication & repetition & packing, unpacking (https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/)
        print()
        len()
        max()
        min()
        sort()

---- > If a function handles more than one datatype & different parameter size the it is polymorphism

Two types of polymorphism

1.Compile time polymorphism or Static polymorphism or static binding
2.Runtime polymorphism or Dynamic polymorphism or dynamic binding

"""

####### '+' symbol polymorphism examples
print('+ symbol polymorphism examples')
print('adding two numbers : ',5+5)
print('concatenate two strings : ','abc'+'def')
print('adding list : ',[1,2,3]+[4,5,6])


####### print function as polymorphism  (Runtime polymorphism example)
print('print function as polymorphism')
print(10)
print(20.5)
print('meme programmers')
print(1,2,3,'hi')

####### example program for polymorphism
class A:
    def add(self,*args):
        if args:
            sum=type(args[0])()
            for i in args:
                sum+=i
            return sum
        
obj=A()
print(obj.add(1,2))
print(obj.add(1,2,3))
print(obj.add('a','b','c'))
print(obj.add('a','b'))
print(obj.add(11.2,2.22,3.1))
print(obj.add([1,2],[3,4]))
print(obj.add(1,2,3,4,5,6,7))


####### Method Overloading program explained


####### Method overriding program explained