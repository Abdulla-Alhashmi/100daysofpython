from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.color('black')
        self.penup()
        self.setposition(-230, 230)
        self.update()

    def update(self):
        self.write(f"Level: {self.score}", font= ("Courier", 24, "normal"))

    def game_over(self):
       self.goto(0, 0)
       self.write(f"GAME OVER", align= 'center', font= FONT)




