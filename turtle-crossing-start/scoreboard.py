FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.score()
     
        
    def score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
    
    def level_up(self):
        self.level += 1
        self.score()

    def gameover(self):
        self.goto(0,0)
        self.write("Gameover", align="center", font=FONT)
