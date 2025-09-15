import turtle

screen = turtle.Screen()
screen.bgcolor("black") # Set background color

my_turtle = turtle.Turtle()
my_turtle.color("white")     # Set pen color
my_turtle.pensize(30)       # Set pen size
my_turtle.speed(100)

for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.back(100)
    my_turtle.left(90)
    my_turtle.back(100)
    my_turtle.right(90)
screen.exitonclick()