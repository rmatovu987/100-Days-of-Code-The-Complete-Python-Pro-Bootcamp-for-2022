import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")

turtle.colormode(255)


def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


for _ in range(36):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading()+10)

screen = Screen()
screen.exitonclick()
