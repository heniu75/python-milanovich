msg = "HelloWorld"
print(msg)
print(" 1.  Capitalizing ... " + msg.capitalize())
print(" 2.  Checking isalpha() ... {0}".format(msg.isalpha()))
print(" 3.  Checking isalpha() ... " + str(msg.isalpha()))
print(" 3b. Checking isalpha() ...", msg.isalpha())
isa = msg.isalpha()
print(f" 3c. Checking isalpha ... {isa}")
print(" 4.  Checking isdigit() ... {0}".format(msg.isdigit()))
print(" 5.  Checking isdigit() ... " + str(msg.isdigit()))
print(" 6.  Replacing e with a ... {0}".format(msg.replace("e", "a")))
print(" 7.  Replacing e with a ... " + msg.replace("e", "a"))

csvValues = "some, csv, values"
splitValues = csvValues.split(",")


# string formatting in python3:
print(f"Illustrating python 3 formatting: {splitValues[0]}, {splitValues[1]}, {splitValues[2]}")