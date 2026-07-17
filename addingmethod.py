class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)

student = Student("Pari")
student.greet()