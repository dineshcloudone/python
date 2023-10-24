numbers = [1,4,5,11,6,7]
numbers.append(20) #append
print(numbers)
numbers.insert(0,10) #insert
print(numbers)
numbers.remove(7) #remove
print(numbers)

print(numbers.index(4)) #you will get Value error if the given value doesn't exist
print( 4 in numbers) # we can check number existence in list 

print(numbers.count(4))


numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2=numbers.copy
print(numbers2)

#numbers.pop() #removes last element
#print(numbers)

#numbers.clear() #removes all elements
#print(numbers)

