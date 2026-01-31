from turtle import *
import random


MOVE_X = 5
SPAWN_CHANCE = 7
LANES = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        colormode(255)
        self.colors_list = [
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
        self.create_car()

    def create_car(self):
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape("square")
        self.color(random.choice(self.colors_list))
        self.penup()
        self.goto(x=300, y=random.choice(LANES))


    def move_car(self):
        new_x = self.xcor() - MOVE_X
        self.goto(new_x, self.ycor())


