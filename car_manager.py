from turtle import *
import random

STARTING_MOVE_DISTANCE = 10
SPAWN_CHANCE = 6
MOVE_INCREMENT = 10
COLORS = [
            (241, 119, 38),
            (240, 77, 93),
            (163, 111, 8),
            (131, 215, 207),
            (239, 96, 29),
            (167, 45, 137),
            (28, 35, 41),
            (85, 183, 6),
            (53, 93, 86),
            (148, 185, 222),
            (134, 216, 221),
            (249, 207, 0),
            (201, 134, 13),
            (247, 210, 40),
            (133, 197, 171),
            (158, 192, 229),
            (233, 165, 177),
            (43, 77, 72),
            (88, 94, 98),
            (240, 171, 156),
            (27, 39, 37),
            (145, 28, 113),
            (119, 97, 0),
            (116, 136, 137),
        ]

class Car():
    def __init__(self):
        colormode(255)
        self.all_cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,SPAWN_CHANCE)

        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.shape("square")
            random.choice(COLORS)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT