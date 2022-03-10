# -*- coding: cp1252 -*-
import turtle

from datetime import datetime
now = datetime.now()

def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)
    

name = input ("what is your name? ")
print ("hello " + name)

age = int(input("And how old are you? "))
location = input ("where do you live? ")
gender = input("What sex are you? ")
year = now.strftime("%Y")
dob = (int(year) - age)


print ("So now we know, ")
print ("Your name is " + name)
print ("You are " + str(age))
print ("You are " + gender)
print ("you where born in " + str(dob))
if gender ==("male"):
    print ("'whats up dude'")
elif gender == ("female"):
    print ("'hey sexy'")
else:
    print ("I don't think thats a gender.")
print ("and you live in " + location)
if location == ('spain'):
    print ("I bet it´s hot there today.")
elif location == ("uk"):
    print ('it\'s probably raining today.')
else:
    print ("I dont know where " + location + " is!")

print
"""
just a bit of useless knowlage for you.
I am telling you this to show you how to print two different
ways.
"""

shopping = ['eggs', 'bacon', 'milk', 'cheese', 'bread', 'sausage', 'chicken', 'fish', 'apples', ]
print ("We have a shopping list")
show_shopping = input("Do you want to see it? ")
if show_shopping == ('yes'):
    for items in shopping:
        print (items)
else:
    print ("Fine Then!")
if show_shopping == ('yes'):
    fav = input("Let's add your favorite food, name it ")
    if len(fav) > 0:
        shopping.append(fav)
        for d in shopping:
            print (d)
    else:
        print ("Dont you like food? You Fool!!")

if show_shopping == ('yes'):
    show_order = input("\nShall we see it in alphabetical order? ")
    if show_order == ('yes'):
        shopping.sort()
        for h in shopping:
            print (h)
    else:
        print ("thats OK maybe later")

if show_shopping == ('yes'):
    remove_3rd = input("Shall we remove the 3rd item in the list? ")
    if remove_3rd == ('yes'):
        del shopping[2]
        for o in shopping:
            print (o)
    else:
        print ("thats OK maybe later")


add_square = input("Shall we draw a square? ")
if add_square == ("yes"):
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    square(100, 90)

    add_circle = input("Ok shall we make a circle out of squares? ")   
    if add_circle == ("yes"):
        for a in range(36):
            square(100, 90)
            my_turtle.right(10)
    else:
        print("you missed a very nice circle!")
else:
    print('Next time then!')



