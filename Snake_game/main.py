from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0,0),(-20,0),(-40,0)]
segments = []

for pos in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)


screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    for seg in range(len(segments)-1, 0, -1):
        new_x = segments[seg-1].xcor()
        new_y = segments[seg-1].ycor()
        segments[seg].goto(new_x,new_y)
    segments[0].forward(20)
        
        
        

# print(segments)
screen.exitonclick()