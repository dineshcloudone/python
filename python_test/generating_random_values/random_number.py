import random

for i in range(3):
    print(random.random()) #generates random value between 0 to 1

print("################################")

for i in range(3):
    print(random.randint(10,20)) #between 10 and 20

print("################################")

members = ['john', 'Mary', 'Bob','Mosh']
leader = random.choice(members) #chooses a leader
print(leader)

