import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tom = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.onkey(tom.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.listen()
    CarManager()
    screen.update()
    cars.create_cars()
    cars.move_cars()

    #Detect collision here
    for car in cars.all_cars:
        if car.distance(tom) < 22:
            game_is_on = False
            scoreboard.game_over()

    if tom.is_at_finishline():
        tom.go_to_start()
        cars.level_up()
        scoreboard.increase_level()





screen.exitonclick()