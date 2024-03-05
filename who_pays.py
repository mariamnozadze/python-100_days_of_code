# write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]



import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"

# Split the string into a list of names
names = names_string.split(", ")

# Get the number of items (names) in the list
num_items = len(names)

# Generate a random index within the range of the list
random_choice = random.randint(0, num_items - 1)
print(names[random_choice])
