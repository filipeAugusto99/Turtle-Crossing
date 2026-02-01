from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.create_character()


    def create_character(self):
        self.speed("fastest")
        self.penup()
        self.shape("turtle")
        self.go_to_start()
        self.setheading(90)

    def move_character_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def move_character_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False