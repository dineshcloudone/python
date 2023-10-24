'''
update() : to update one dictionary with second dictionary values
    Syntax :
        dictionary1.update(dictionary2)

fromkeys() : to assign same value for all keys
    Syntax :
        dic.fromkeys(iterable,value)

    dict - dictionary class
    iterable - list/set/tuple/string/range/array etc
    value - value we want to store in keys, default value is None

popitem() : to remove last item in a dictionary
pop() : to remove any item using key
    Syntax :
        dictionary.pop(key)
clear()
'''

# update
dictionary1={'a':1,'b':2}
dictionary2={'a':1,'b':2}

print(dictionary1.update(dictionary2)) #output : None
print(dictionary1) #output : {'a': 1, 'b': 2}

# from keys
print(' from keys')
print(dict.fromkeys((1,2,3,4),['a','b'])) #output : {1: ['a', 'b'], 2: ['a', 'b'], 3: ['a', 'b'], 4: ['a', 'b']}

print(dict.fromkeys('memeprogrammers',{1,2})) #output : {'m': {1, 2}, 'e': {1, 2}, 'p': {1, 2}, 'r': {1, 2}, 'o': {1, 2}, 'g': {1, 2}, 'a': {1, 2}, 's': {1, 2}}

#pop
dictionary2.pop('b') #output :2 (removes item 'b':2) if key doesn't exist then it will give error

