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

b=10
c=type(b)()
print(type(b))
print(type(c))
print(id(c))
# print(b)
# print(id(b))
# b=11
# print(b)
# print(id(b))

############ checking concatenation of variables with string

a={1:1,2:2}
print(f'list values:{a}')