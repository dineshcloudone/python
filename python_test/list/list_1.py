names = ['dinesh','kumar','gurram','bob','mosh']
print(names)
print(names[0])
print(names[-1])
print(names[1:2]) #it will not consider index 2 to print the second value
print(names[-4:-1]) #it will not consider index -1 to print the second value
print(names[-2:])
print(names[:])
#Modifying the list items
names[4]="test"
print(names[:])