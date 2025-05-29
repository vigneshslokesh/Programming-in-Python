from turtle import Turtle,Screen
import random

turtle = Turtle()

colour = ["red", "black", "pink", "blue", "green", "orange", "grey", "purple", "coral"]
def draw_shape(num):
    angle = 360 / num
    for _ in range(num):
        turtle.right(angle)
        turtle.forward(100)


for i in range(3,11):
    turtle.color(random.choice(colour))
    draw_shape(i)


screen = Screen()
screen.exitonclick()
