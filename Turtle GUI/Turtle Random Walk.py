from turtle import Turtle, Screen
import random

turtle = Turtle()
directions = [0, 90, 180, 270]
colour = ["red", "black", "pink", "blue", "green", "orange", "grey", "purple", "coral"]
turtle.speed(6)


turtle.pensize(10)

for i in range(200):
    turtle.color(random.choice(colour))
    turtle.setheading(random.choice(directions))
    turtle.forward(20)




screen = Screen()
screen.exitonclick()