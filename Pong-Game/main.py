from turtle import Turtle, Screen
import time
from paddle import Paddle

screen = Screen()


screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Pong")
screen.tracer(0)


paddle_1 = Paddle(280)
paddle_2 = Paddle(-280)


    

screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

game_is_on =True
while game_is_on:
    screen.update()

screen.exitonclick()
