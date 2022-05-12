from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, direction: str):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if direction and direction == 'left':
            self.goto(-350, 0)
        elif direction and direction == 'right':
            self.goto(350, 0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

