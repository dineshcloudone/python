class Vector:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self,other): #likewise we can create sub, mult, div
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"x: {self.x}, y:{self.y}"

    def __call__(self):
        print(f" hello I am called !")
    
v1 = Vector(10,20)
v2 = Vector(40,40)
v3 = Vector(30,50)
v4 = v1 + v2 + v3

print(v4.x)
print(v4.y)

print(v4)

v4()