rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
list = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0,2)

if your_choice >=0 and your_choice <=2:
  print(f"\nYou chose\n {list[your_choice]}\nComputer chose\n {list[computer_choice]}")
  if your_choice == 0 and computer_choice == 2:
    print("You Win")
  elif your_choice == 1 and computer_choice  == 0:
    print("You Win")
  elif your_choice == 2 and computer_choice == 1:
    print("You Win")
  elif your_choice == computer_choice:
    print("Its a draw")
  else:
    print("You Loose")
else:
  print("That number is't one that we asked for")

  
