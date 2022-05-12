import random
from turtle import Turtle


class Food(Turtle):
    """Food class that inherits from Turtle class"""

    def __init__(self):
        """Food class constructor"""
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Refresh food location"""
        self.goto(random.randint(-500, 500), random.randint(-500, 500))