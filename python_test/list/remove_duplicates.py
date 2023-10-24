numbers = [1,3,4,2,3,2]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
