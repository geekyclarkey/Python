

print ("\nHello, welcome to the Clarke brothers Lumen Calculator!\n")
print ("First lets work out the size of your room you wish to brighten\n")


length = input("In meters, What is the length of the room? ")
width = input("And the width? ")

room_size = int(length) * int(width)

print("\nso, your room is " + str(room_size) + " meters squared")

#This is to convert meters to feet because the numbers below need to be feet
length = int(length) * 3.28084
width = int(width) * 3.28084
room_size = int(length) * int(width)

print ("""
Here we have some room types:
------------------
1 - Livingroom
2 - Kitchen
3 - Dining Room
4 - Bedroom
5 - Hallway
6 - Bathroom
------------------
""")

room_type = int(input("Choose the room type from the list above? Please use the number "))
if room_type == 1 or 4:
   room1 = 10
   room2 = 20
if room_type == 2 or 3:
   room1 = 30
   room2 = 40
if room_type == 5:
   room1 = 5
   room2 = 10
if room_type == 6:
   room1 = 70
   room2 = 80


total1 = int(room_size) * int(room1)
total2 = int(room_size) * int(room2)
average = (total1 + total2) / 2

print ("\nOK, for optimum light your bulb needs to be between " + str(total1) + " and " + str(total2) + " lumens\n")
print (str(total1) + " lumens is the dimest bulb you should have")
print (str(total2) + " lumens is the brightest bulb you should have\n")
print ("The average between the dimest and brightest is " + str(int(average)))
print ("\nRemember if you have more than 1 light socket in that room, you can split the limens into multiple light sockets")
