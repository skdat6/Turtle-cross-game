FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.speed("fastest")
        self.text = "Level: "
        self.pu()
        self.level = 1
        self.setpos(-290, 250)
        self.write(self.text + str(self.level), align="left", font=("Arial", 30, "normal"))


    def reset(self):
        self.level = 1

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(self.text + str(self.level), align="left", font=("Arial", 30, "normal"))