students = {
    "Ram": 78,
    "Sita": 92,
    "Hari": 85,
    "Gita": 88,
    "Anil": 75
}

total = 0
highest_student = ""
highest_marks = 0

for name, marks in students.items():
    total += marks

    if marks > highest_marks:
        highest_marks = marks
        highest_student = name

average = total / len(students)

print("Student with highest marks:", highest_student)
print("Highest marks:", highest_marks)
print("Average marks:", average)