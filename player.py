from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.pu()
        self.setpos(STARTING_POSITION)

    #Move turtle
    def player_move_up(self):
        self.forward(MOVE_DISTANCE)

    #Reset game
    def reset(self):
        self.setpos(STARTING_POSITION)

