from turtle import  Turtle

STARTING_POSITION = (-40, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.start_point = STARTING_POSITION
        self.setposition(self.start_point)

    def move(self):
        self.forward(20)




