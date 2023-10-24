'''
range() : this function is used to generate a sequence of numbers
It is mainly used in for loop

    Syntax : It only supports int
    range(start, stop, step)
        start : default is 0
        stop : upto given number (less than that number)
        step : default value is 1

range() : it is an iterable
'''
print(list(range(5))) #output : [0, 1, 2, 3, 4]
print(list(range(0,5))) #output : [0, 1, 2, 3, 4]

for i in range(10):
    print('meme programmers')
