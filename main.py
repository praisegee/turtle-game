import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision between the turtle and the cars
    for car in car_manager.car_lists:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect if turtle get to the finish line
    if player.is_at_finish_line():
        scoreboard.increment_level()
        player.goto_starting_position()
        car_manager.level_up()




screen.exitonclick()
