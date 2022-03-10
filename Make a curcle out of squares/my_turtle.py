import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

# Here is 2 ways to start the script

# for i in range(400):
#    square(length = 100, angle = 90)
#    my_turtle.right(11)

while 1 == 1:
    square(100, 90)
    my_turtle.right(22)
