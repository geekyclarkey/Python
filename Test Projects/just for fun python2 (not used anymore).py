# -*- coding: cp1252 -*-

name = raw_input ("what is your name? ")
print "hello " + name

age = input("\nand how old are you? ")
location = raw_input ("where do you live? ")
gender = raw_input("What sex are you? ")
ageee = 2015 - age

print "So now we know,"
print "Your name is " + name
print "You are " + `age` + ", whitch means you where  born in " + `ageee`
print "You are " + gender
if gender ==("male"):
    print "'whats up dude'"
elif gender == ("female"):
    print "'hey sexy'"
else:
    print "I don't think thats a gender."
print "and you live in " + location
if location == ('spain'):
    print "I bet it´s hot there today."
elif location == ("uk"):
    print 'it\'s probably raining today.'
else:
    print "I dont know where " + location + " is!"

import math
agee = math.sqrt(age)
print "Did you know that the square root for your age is... " + `agee`

print """
just a bit of useless knowlage for you.
I am telling you this to show you how to print two different
ways.
"""

shopping = ['eggs', 'bacon', 'milk', 'cheese', 'bread', 'sausage', 'chicken', 'fish', 'apples', ]
print "\nWe have a shopping list"

show_shopping = raw_input("Do you want to see it? ")
if show_shopping == ('yes'):
    for s in shopping:
        print s

    show_order = raw_input("\nShall we see it in alphabetical order? ")
    if show_order == ('yes'):
        shopping.sort()
        for h in shopping:
            print h
else:
    print "thats OK maybe later"

fav = raw_input("Let's add your favorite food, name it ")
shopping.append(fav)

print shopping

remove_3rd = raw_input ("\nShall we remove the 3rd item in the list? ")
if remove_3rd == ('yes'):
    del shopping [2]
    for o in shopping:
        print o
else:
    print "thats OK maybe later"

fav = raw_input("Let's add your favorite food, name it ")
shopping.append(fav)

print shopping
    
