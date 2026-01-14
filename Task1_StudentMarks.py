# Task 1: Dictionary of student marks

# Creating a dictionary of student marks
student_marks = {
    "Neha": 85,
    "Amit": 78,
    "Pooja": 92,
    "Rahul": 88
}

# Taking student name as input
name = input("Enter student name: ")

# Retrieving and displaying marks
if name in student_marks:
    print(f"Marks of {name}: {student_marks[name]}")
else:
    print("Student not found in the record.")
