food = {"ham": "yes", "egg": "yes", "spam": "no"}

for foodItem in food:
    print(foodItem)

for key in food.keys():
    print(key)

for value in food.values():
    print(value)

# print it
print(food)

# add an item
food["fights"] = "of course"
print(food)

# update an item
food["fights"] = "yes"
print(food)

# remove an item
del food["fights"]
print(food)

# test a key exists in the dictionary
if "fights" in food:
    print("fights are in food")
else:
    print("fights are not in food")
