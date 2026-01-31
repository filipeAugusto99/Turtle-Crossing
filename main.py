# Step 01 - Set up the main screen
from turtle import Screen
from character import Character
from cars import Car
from scorelevel import ScoreLevel
import random
import time
import cars


scr = Screen()
scr.setup(width=600, height=600)
scr.tracer(0)


# Step 02 - Creating the turtle and move it
player = Character()
score = ScoreLevel()
cars_list = []


scr.listen()
scr.onkey(player.move_character_up, "Up")
scr.onkey(player.move_character_down, "Down")


game_is_on = True


while game_is_on:
    scr.update()
    time.sleep(0.07)

    # this condition and this for loop spawn cars
    if random.randint(1, cars.SPAWN_CHANCE) == 1:
        cars_list.append(Car())

    for car in cars_list:
        car.move_car()

    # remove cars when get out of the screen
    for car in cars_list:
        if car.xcor() < -320:
            car.hideturtle()
            cars_list.remove(car)


    # collision when character player hit the car
    for car in cars_list:
        if car.distance(player) < 25:
            game_is_on = False
            score.game_over()

    # collision when turtle goes out of the bounds
    if player.ycor() > 290:
        score.increase_level()
        player.goto((0, -280))

scr.exitonclick()