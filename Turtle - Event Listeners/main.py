import turtle as t

tim = t.Turtle()
#tim - turtle
screen = t.Screen()


def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()