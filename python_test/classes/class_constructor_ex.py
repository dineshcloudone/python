class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

#point = Point(10,20)

points = [Point(10,20), Point(30,40)]

for p in points:
    p.x = 11
    print(p.x)
    print(p.y)
