
fruits = ["Apples", "Bananas", "Peaches"]
for item in fruits:
    print(item)
# This will cycle through the list and rename each item "item" and print it to the console down in a line.
# for an example see average checker

for number in range(1, 101):# You need to put 101 because the last number isnt counted
    print(number)
# This will go through each number 1-100 and print it one at a time

vegtables = ["Potatoes", "Carots", "Onions"]
shopping_list = [fruits, vegtables]

# To pick out a single item in a list you use:
choice = vegtables[0] #This will choose "Potatoes"

import random # Remember to import random!
random_veg = random.choice(vegtables) # The random.choice will choose a random item from the vegtables list
random_int = random.randint(1, 10) # the randint will choose a random integer between the given range

name = "Sean"
spiders = 22
if "Potatoes" in vegtables:
    print("Its there!")
    if 1 > 5 and 10 == 10:
        name = name + " smells"
    elif spiders % 2 == 0: # The modulo means the number goes into spiders and == 0 means there are no remainders
        name = name + " is great!"
else:
    print("Not in there!")
# This is a nested if statement. you dont always need an else!