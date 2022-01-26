from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []


    def create(self):
        random_pick = randint(1,7)
        if random_pick == 5 or random_pick == 4:
            car_unit = Turtle(shape='square')
            car_unit.shapesize(stretch_len=2)
            car_unit.color(choice(COLORS))
            car_unit.penup()
            car_unit.setposition(x=300, y=randint(-200, 200))
            car_unit.seth(180)
            self.car_list.append(car_unit)

    def move(self):
        global MOVE_INCREMENT
        for i in self.car_list:
            i.forward(MOVE_INCREMENT)
            # print(i.position())
            # if i.xcor() < -300:
            #     i.setposition(300, randint(-250, 250))
