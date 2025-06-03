import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
user_ip = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

is_race_on = False
color= ['red','yellow','blue','green','purple','orange']
turtles = []
y = -100
for i in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[i])
    new_turtle.goto(-230, y)
    y += 35
    turtles.append(new_turtle)

if user_ip:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_ip == winning_color:
                print(f"You win!, The {winning_color} turtle is the winner.")
            else:
                print(f"You loose!, The {winning_color} turtle is the winner.")


        steps = random.randint(1,10)
        turtle.forward(steps)

screen.exitonclick()