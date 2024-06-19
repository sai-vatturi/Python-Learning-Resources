class Student:
    
    def __init__(self, name: str, id: int, address: str):
        self.name = name
        self.id = id
        self.address = address

    def study(self):
        print(self.name, "is studying.")

    def run(self):
        print(self.id, "is student's id.")

    def location(self):
        print(self.address, "is the student's location.")

    def __str__(self) -> str:
        return f"Student(name={self.name}, id={self.id}, address={self.address})"