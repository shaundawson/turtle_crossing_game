from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.right(270)
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
