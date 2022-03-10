continue_on = True

answer1= input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()

if answer1 == "left":
  answer2 = input('You have come to a river, what do you want to do? type "wait" to wait for a boat or "swim" to swim accross\n').lower()
  if answer2 == "wait":
    answer3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow & one blue. Which colour do you choose?\n').lower()
    if answer3 == "red":
      print("You have stepped into a room of lava, Game Over!!!")
      continue_on = False
    elif answer3 == "blue":
      print("You have entered a room full of beasts, Game Over!!!")
      continue_on = False
    elif answer3 == "yellow":
      print("You found the treasure, Well done!")
    else:
      print("thats not a door, Game Over!!!")
      continue_on = False
  else:
    print("You got eaten by a crocodile, Game Over!!!")
    continue_on = False
else:
  print("You fell down a hole! Game Over!!!")
  continue_on = False