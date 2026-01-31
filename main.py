# Step 01 - Set up the main screen
from turtle import Screen
from character import Character

scr = Screen()
scr.setup(width=600, height=600)


# Step 02 - Creating the turtle and move it
tim = Character()


scr.listen()
scr.onkey(tim.move_character_up, "Up")
scr.onkey(tim.move_character_down, "Down")


scr.exitonclick()