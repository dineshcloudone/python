#tuples are immutable, you cannot modify them
numbers = (1,2,3)
numbers[0]=10
print(numbers) # will print "TypeError: 'tuple' object does not support item assignment"