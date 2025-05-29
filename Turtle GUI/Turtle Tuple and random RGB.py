import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

turtle_obj = Turtle()
directions = [0, 90, 180, 270]
# colour = ["red", "black", "pink", "blue", "green", "orange", "grey", "purple", "coral"]
turtle_obj.speed(6)


turtle_obj.pensize(10)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_col = (r,g,b)
    return random_col

for i in range(200):
    turtle_obj.color(random_color())
    turtle_obj.setheading(random.choice(directions))
    turtle_obj.forward(20)




screen = Screen()
screen.exitonclick()