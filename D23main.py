import time
from turtle import Screen
from D23player import Player
from D23car_manager import CarManager
from D23scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy = Player()
screen.listen()
car = CarManager()
fast = 0.1
scoreboard = Scoreboard()

screen.onkey(timmy.move, 'Up')


score = 0
game_is_on = True

while game_is_on:
    car.create()
    car.move()
    if timmy.ycor() > 280:
        scoreboard.score += 1
        fast *= 0.9
        timmy.setposition(timmy.start_point)
        scoreboard.clear()
        scoreboard.update()
    for i in car.car_list:
        if timmy.distance(i) < 20:
            game_is_on = False
            scoreboard.game_over()
    time.sleep(fast)
    screen.update()



screen.exitonclick()
