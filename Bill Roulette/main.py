import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_len = len(names)
random_number = random.randint(0, (names_len -1))
random_name = names[random_number]

print(f"{random_name} is going to buy the meal today!")

# or

# random_name = random.choice(names)
# print(f"{random_name} is going to buy the meal today!")
