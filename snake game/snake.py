from turtle import Turtle


class Snake:
    """The Snake Class"""

    POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        """The constructor"""
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        """Method that creates the snake"""
        for pos in self.POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        t1 = Turtle('square')
        t1.color('white')
        t1.penup()
        t1.goto(position)
        self.segment.append(t1)

    def detect_collision(self) -> bool:
        for seg in self.segment:
            if seg is not self.segment[0] and self.segment[0].position() == seg.position():
                return True
        return False

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        """Method to move the segments"""
        for s in range(len(self.segment) - 1, 0, -1):
            self.segment[s].goto(self.segment[s - 1].xcor(), self.segment[s - 1].ycor())
        self.head.forward(self.MOVE_DISTANCE)

    def up(self):
        """Method to change up"""
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def down(self):
        """Method to change down"""
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def left(self):
        """Method to change left"""
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def right(self):
        """Method to change right"""
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)
