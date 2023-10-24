class Person:
    
    def __init__(self, name, age) -> None:
        self.name=name
        self.age=age

    def __del__(self):
        print("Object is being deleted")

p =Person("python",15)

#manual deletion of object p --> del p
print(p.name)
print(p.age)