class Student:
    def __init__(self, name, age, marks) -> None:
        self.name = name
        self.age = age
        self.marks = marks

    def get_grade(self):
        return self.marks

class Course:
    def __init__(self, name, max_students) -> None:
        self.course_name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False
        
    def get_student_names(self):
        for student in self.students:
            print(student.name)

    def get_average(self):
        total = 0
        for student in  self.students:
            total += student.marks
        return total / len(self.students)

s1 = Student("Sai", 21, 85)
s2 = Student("Himalesh", 20, 95)
s3 = Student("Preran", 19, 75)

c1 = Course("Maths", 2)

c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)

c1.get_student_names()
print(c1.get_average())