from turtle import Turtle

class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("turtle")
        self.goto(0, -280)
        self.setheading(90)


    def move_character_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def move_character_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
