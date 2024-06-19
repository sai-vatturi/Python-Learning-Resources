class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("I don't know what sound to make")

    def get_details(self):
        print(f"I am {self.name} and i am {self.age} years old.")


class Dog(Pet):
    def make_sound(self):
        print("Boow! Bow")

    def fetch(self):
        print("I am fetching!")

class Cat(Pet):
    def make_sound(self):
        print("Meow")
    
    def catch(self):
        print("I am catching")

p = Pet("Pett", 2)
p.make_sound()
p.get_details()

d = Dog("Chinnu", 2)
d.get_details()
d.make_sound()
d.fetch()

c = Cat("Choco", 3)
c.get_details()
c.make_sound()
c.catch()