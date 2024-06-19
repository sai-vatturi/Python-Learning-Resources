class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"The Dog {self.name} is Barking!")

d = Dog("Chinnu", 1)

d.bark()
# print(type(d.bark()))