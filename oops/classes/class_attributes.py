class Person:
    no_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name    
        Person.add_person()

    
    @classmethod
    def no_of_people_(cls):
        return cls.no_of_people
    
    @classmethod
    def add_person(cls):
        cls.no_of_people += 1

p1 =  Person("Sai")
p2 = Person("Himalesh")
p3 = Person("Preran")

print(Person.no_of_people_())