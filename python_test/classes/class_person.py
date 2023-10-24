class Person:

    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hi ! i am {self.name}")

john = Person("john")
john.talk()

tim = Person("Tim")
john.talk()