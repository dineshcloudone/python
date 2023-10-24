"""
in print by default end='\n' will be there

* - unpacking operator ex : print(*[1,2,3,4]) -> print(1,2,3,4)
"""

print(10)

a=1
print(a)

print(a,20,30)

for i in [1,2,3,4]:
    print(i,end=' ')
print()

print('python',end=',')
print('learning')

#printing list elements separating with space
#

print(*[1,2,3,4]) #unpacked to print(1,2,3,4)

#printing list elements separated with comma
print(*[1,2,3,4],sep=',')
print('python','learning',sep=',')

#to save output to a file
file=open("/root/workspace/python_memeprgrm/samplefile.txt",'w')
print(*[1,2,3,4],sep=',',file=file) 
file.close()


