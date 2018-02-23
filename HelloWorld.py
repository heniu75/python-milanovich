# HelloWorld.py
csvValues = "some, csv, values"
splitValues = csvValues.split(",")

# simple looping
for item in splitValues:
    print(item.strip())

# indexed for looping
for x in range(0, len(splitValues)):
    print(x, splitValues[x].strip())

# boolean

a = True
b = False

aliens_found = None

# if then else
number = "" # this is not very truthy

print(f"The number is defined as '{number}'")

if number == 5:
    print("The number is 5")
else:
    print("The number is not 5")

# truthy vs false
if number:
    print("The number's value is truthy")
else:
    print("The number's value is not truthy")

# ternary operator
a = 2
b = 4
out = "bigger" if a > b else "smaller"
print(f"Ternary operator test: a ({a}) is {out} than b {b}")


