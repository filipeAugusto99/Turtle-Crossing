# Step 01 - Set up the main screen
from turtle import Screen
from character import Character
from car_manager import Car
from scorelevel import ScoreLevel
import random
import time
import car_manager


scr = Screen()
scr.setup(width=600, height=600)
scr.tracer(0)


# Step 02 - Creating the turtle and move it
player = Character()
car_manager = Car()
score = ScoreLevel()

scr.listen()
scr.onkey(player.move_character_up, "Up")
scr.onkey(player.move_character_down, "Down")


game_is_on = True


while game_is_on:
    scr.update()
    time.sleep(0.07)

    car_manager.create_car()
    car_manager.move_cars()


    # collision when character player hit the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # collision when turtle goes out of the bounds
    if player.is_at_finish_line():
        player.go_to_start()
        score.increase_level()
        car_manager.level_up()

scr.exitonclick()