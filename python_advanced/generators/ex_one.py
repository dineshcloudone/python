import sys

def mygenerator(n):
    for x in range(1,n):
        yield x ** 2
        
values = mygenerator(20)

print("bytes:"+str(sys.getsizeof(values))) #128 Bytes size always

# print(next(values)) #next is keyword to get next value
# print(next(values))
# print(next(values))

for x in values:
    print(x)
    
print("bytes:"+str(sys.getsizeof(values)))