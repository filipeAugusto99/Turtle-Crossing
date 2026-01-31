from turtle import Turtle
import random


MOVE_X = 5
SPAWN_CHANCE = 10
LANES = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()


    def create_car(self):
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape("square")
        self.color("black")
        self.penup()
        self.goto(x=300, y=random.choice(LANES))


    def move_car(self):
        new_x = self.xcor() - MOVE_X
        self.goto(new_x, self.ycor())


