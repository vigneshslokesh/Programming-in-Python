from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball

screen = Screen()


screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)


paddle_1 = Paddle((380,0))
paddle_2 = Paddle((-380,0)) 
ball = Ball()

    

screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

game_is_on =True
while game_is_on:
    time.sleep(0.04)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(paddle_1)<37 and ball.xcor() > 320 and ball.x_move > 0) or (ball.distance(paddle_2)<37 and ball.xcor() < -320 and ball.x_move < 0):
        ball.hit()

    if ball.xcor() > 380:
        ball.reset()

    if ball.xcor() < -380:
        ball.reset()

screen.exitonclick()
