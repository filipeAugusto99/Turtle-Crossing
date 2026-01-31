from turtle import Turtle

class ScoreLevel(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score_level = 0
        self.update_level()



    def update_level(self):
        self.clear()
        self.goto(x= -250, y=250)
        self.write(f"Level {self.score_level}", align="left", font=("Courier", 24, "normal"))


    def increase_level(self):
        self.score_level += 1
        self.update_level()


    def game_over(self):
        self.goto(x=-0, y=0)
        self.color("red")
        self.write("GAME OVER!", align="center", font=("Courier", 48, "normal"))
