import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

turtle_obj = Turtle()

turtle_obj.speed(0)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turtle_obj.color(random_color())
        turtle_obj.circle(100)
        turtle_obj.setheading(turtle_obj.heading()+size_of_gap)

draw_spirograph(5)
    





screen = Screen()
screen.exitonclick()