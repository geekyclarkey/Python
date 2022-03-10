

print ("""\nHello, welcome to the Clarke brothers Lumen Calculator!
First lets work out the size of your room you wish to brighten""")

def calculate():
   length = input("\nIn meters, What is the length of the room? ")
   width = input("And in meters, the width? ")

   room_size = float(length) * float(width)
   room_size = ("%.1f" % room_size) 

   print("\nSo, your room is " + str(float(room_size)) + " meters squared")

   #print (length)
   #print (width)
   #print (room_size)


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

   if room_type == 1:
      room1 = 108
      room2 = 215
   if room_type == 2:
      room1 = 322
      room2 = 430
   if room_type == 3:
      room1 = 322
      room2 = 430
   if room_type == 4:
      room1 = 108
      room2 = 215
   if room_type == 5:
      room1 = 53
      room2 = 108
   if room_type == 6:
      room1 = 753
      room2 = 861

   #print (room1)
   #print (room2)


   total1 = float(room_size) * room1
   total2 = float(room_size) * room2
   average = (total1 + total2) / 2

   #print (total1)
   #print(total2)
   #print(average)

   print ("\nOK, for optimum light your bulb needs to be between " + str(int(total1)) + " and " + str(int(total2)) + " lumens\n")
   print (str(int(total1)) + " lumens is the dimest bulb you should have")
   print (str(int(total2)) + " lumens is the brightest bulb you should have\n")
   print ("The average between the dimest and brightest is " + str(int(average)))
   print ("\nRemember if you have more than 1 light socket in that room, you can split the limens into multiple light sockets")
   
while 1==1:
   calculate()
