# write a program that will mark a spot on a map with an X.

# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# This is a bit hard to work with. code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.
# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# Your job is to write a program that allows you to mark a square on the map using a letter-number system.
# First, your program must take the user input and convert it to a usable format.

# Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# -- Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:

# list = [['A', 'B, 'C'], 'E', 'F', 'G']
# E is list[1] C is list[0][2]

# Check your formatting. This is correctly formatted:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']


# ------------------
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print(f"{line1}\n{line2}\n{line3}")
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? e.g. A2, B3 or etc..  ")

letter = position[0].lower() #  Extract the first character and convert it into the lowercase
abc = ["a", "b", "c"]
letter_index = abc.index(letter)       # Find the index of the extracted letter in the list
number_index = int(position[1]) - 1    # Extract the input's second character, convert it to an integer
map[number_index][letter_index] = "X"  # Update the map by placing an "X" at the specified location.

print(f"{line1}\n{line2}\n{line3}")