numbers = [5,2,5,2,2]
for n in numbers:
    print("x" * n)

print("\n \n")

numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)