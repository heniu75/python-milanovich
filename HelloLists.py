# lists
student_names = ["mark", "bob", "katerina"]
print(student_names)
student_names[2] = "jen"
print(student_names)
student_names.append("jenna")
print(student_names)
student_names.append(45)
print(student_names)

if "mark" in student_names:
    print("Yes, mark is in student_names")

print("deleting item at index 2 from list")
del student_names[2]
print(student_names)


# sublists

# all items except first
print(student_names[1:])

# all items except first and last
print(student_names[1:-1])

for name in student_names:
    print(f"The student name is {name}")

for x in range(10):
    print(f"x is {x}")