import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
# screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

color= ['red','yellow','blue','green','purple','orange']
y = -100
for i in range(6):
    tim = t.Turtle(shape="turtle")
    tim.penup()
    tim.color(color[i])
    tim.goto(-230, y)
    y += 35

screen.exitonclick()