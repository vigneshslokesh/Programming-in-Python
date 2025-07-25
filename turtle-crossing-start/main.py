import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1) 
    screen.update()

    car.create_cars()
    car.move_cars()

    for c in car.all_cars:
        if player.distance(c)<25:
            player.reset()
            score.gameover()
            game_is_on = False
    
    #Successfull crossing
    if player.finish():
        player.reset()
        car.level_up()
        score.level_up()
            

screen.exitonclick()