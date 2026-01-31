# Step 01 - Set up the main screen
from turtle import Screen

import cars
from character import Character
from cars import Car
import random
import time


scr = Screen()
scr.setup(width=600, height=600)
scr.tracer(0)


# Step 02 - Creating the turtle and move it
tim = Character()
cars_list = []


scr.listen()
scr.onkey(tim.move_character_up, "Up")
scr.onkey(tim.move_character_down, "Down")


game_is_on = True


while game_is_on:
    scr.update()
    time.sleep(0.07)

    # this condition and this for loop spawn cars
    if random.randint(1, cars.SPAWN_CHANCE) == 1:
        cars_list.append(Car())

    for car in cars_list:
        car.move_car()

scr.exitonclick()