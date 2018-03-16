
# Turtle Recursion (33pts)

# 1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (15pts)
# my_screen.clear()

import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.shape("turtle")
my_turtle.showturtle()
my_screen = turtle.Screen()
my_screen.bgcolor('white')


def recursive_h(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + (size / 2), y)
        my_turtle.goto(x + (size / 2), y + (size / 2))
        my_turtle.goto(x + (size / 2), y - (size / 2))
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x - (size / 2), y)
        my_turtle.goto(x - (size / 2) , y - (size / 2))
        my_turtle.goto(x - (size / 2), y + (size / 2))
        recursive_h(x + (size / 2), y + (size / 2), (size / 2), depth - 1)
        recursive_h(x + (size / 2) , y - (size / 2), (size / 2), depth - 1)
        recursive_h(x - (size / 2), y + (size / 2), (size / 2), depth - 1)
        recursive_h(x - (size / 2), y - (size / 2), (size / 2), depth - 1)


recursive_h(0, 0, 350, 4)

my_screen.clear()

# 2)  Using the turtle library, create any of the other recursive patterns in the data folder.
# Challenge yourself to match your pattern as closely as you can to the image.  (15pts)
# Note:  The Koch snowflake shows step by step building of the fractal.
# The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)


my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.shape("turtle")
my_turtle.showturtle()
my_screen = turtle.Screen()
my_screen.bgcolor('white')


my_turtle.goto(-300, -300)


def recursive_escher(size, depth):
    if depth > 0:
        my_turtle.fd(size)
        my_turtle.left(90)
        my_turtle.fd(size)
        my_turtle.left(90)
        my_turtle.fd(size)
        my_turtle.left(90)
        my_turtle.fd(size)
        my_turtle.left(90)
        my_turtle.fd(size / 2)
        my_turtle.left(45)
        recursive_escher((2 * ((size / 2) ** 2)) ** 0.5, depth - 1)


recursive_escher(600, 10)

my_screen.clear()


# 3)  Create your own work of art with a repeating pattern of your making.
# It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.
# Take this one as seriously as the points indicate.  Play around.  (3pt)

# Give all your fractals a depth of at least 4.  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
# All three recursive drawings can be on the same program.  Just use screen.clear() between problems.
# Have fun!
 
# Resource to help you out >>> https://docs.python.org/3.3/library/turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.shape("turtle")
my_turtle.showturtle()
my_screen = turtle.Screen()
my_screen.bgcolor('white')


def recursive_lollipop(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.fd(size)
        my_turtle.right(90)
        my_turtle.fillcolor("pink")
        my_turtle.begin_fill()
        my_turtle.circle(size / 2, 360, None)
        my_turtle.end_fill()
        my_turtle.right(90)
        my_turtle.fd(size)
        my_turtle.right(170)
        recursive_lollipop(x, y, size * 0.97, depth - 1)


recursive_lollipop(0, 0, 350, 100)


my_screen.exitonclick()