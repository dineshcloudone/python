#simple types in python are below
# Numbers
# Strings
# Booleans

# --------------

#couple of complex things in python are below
# Lists
# Dictionaries

#for variables and functions we use lower case letters, words separated with underscore

class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10 #setting attribute
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 11
print(point2.x)

