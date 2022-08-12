import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=2.3)
        self.setheading(180)
        self.setpos(random.randint(280, 320), random.randint(-250, 250))
        self.move_speed = STARTING_MOVE_DISTANCE

    def reset(self):
        pass

    #Choose random color for car model and move car
    def move_car(self):
        self.color(random.choice(COLORS))
        self.forward(self.move_speed)

    #Increment level upon reaching finish
    def level_up(self):
        self.move_speed += MOVE_INCREMENT

