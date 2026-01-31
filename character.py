from turtle import Turtle


MOVE_DISTANCE = 20


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.create_character()


    def create_character(self):
        self.speed("fastest")
        self.penup()
        self.shape("turtle")
        self.goto(0, -280)
        self.setheading(90)

    def move_character_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def move_character_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
