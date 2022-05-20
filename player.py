from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Player class the controls the functionalities of the turtle.
    """
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        """move the turtle up across the screen"""
        self.forward(MOVE_DISTANCE)
        # new_x = self.xcor()
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(new_x, new_y)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_starting_position(self):
        self.goto(STARTING_POSITION)



