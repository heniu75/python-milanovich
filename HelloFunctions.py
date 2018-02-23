# HelloFunctions.py

username = "heniu"

if not username:
    username = input("Enter a user name: ")

print(f"Hello, {username}")

students = []


def add_student(name):
    students.append(name)


def print_students():
    for student in students:
        print(student)


def add(a, b):
    return a+b


add_student("jenna")
add_student("madison")
add_student("emma")
add_student("james")

print_students()
