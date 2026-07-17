class Student:

    def __init__(self, name):
        self.name = name

student = Student("Alice")

print(student.name)

student.name = "Bob"

print(student.name)