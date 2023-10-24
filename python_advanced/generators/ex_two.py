def infinite_squence():
    result = 1
    while True:
        yield result
        result *=5

values = infinite_squence()

# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))


for x in range(40):
    print(next(values))