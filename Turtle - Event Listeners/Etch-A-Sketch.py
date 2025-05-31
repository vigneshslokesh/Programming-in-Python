import turtle as t

tim = t.Turtle()
screen = t.Screen()

def mov_forward():
    tim.forward(15)
def mov_backward():
    tim.backward(15)
def right():
    tim.setheading(tim.heading() +10)
def left():
    tim.setheading(tim.heading() - 10)
def clear():
    tim.clear()

screen.listen()
screen.onkey(key="a",fun=right)
screen.onkey(key="d",fun=left)
screen.onkey(key="w",fun=mov_forward)
screen.onkey(key="s",fun=mov_backward)
screen.onkey(key="c", fun=clear)

screen.exitonclick()