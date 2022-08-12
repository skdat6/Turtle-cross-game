import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

spawned_cars = []
count = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()


screen.listen() ##check for inputs
screen.onkeypress(player.player_move_up, "Up")


game_is_on = True
while game_is_on:


    if count % 6 == 0:
        car = CarManager()
        spawned_cars.append(car)

    #Check if player collides with car
    for i in spawned_cars:
        i.move_car()
        if player.distance(i) < 10:
            print("game over")
            for car in spawned_cars:
                car.setpos(799, 799)
            spawned_cars = []
            game_is_on = False


    #Increment level and car difficulty upon reaching finish
    if player.ycor() >= 280:
        score.level_up()
        car.level_up()
        player.reset()
        for car in spawned_cars:
            car.setpos(799, 799)
        spawned_cars = []



    time.sleep(0.1)
    screen.update()
    count += 1

screen.exitonclick()