from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_up():
    tim.left(10)


def move_down():
    tim.right(10)


def move_back():
    tim.back(10)


screen.listen()
screen.onkey(move_forward, 'Right')
screen.onkey(move_up, 'Up')
screen.onkey(move_back, 'Left')
screen.onkey(move_down, 'Down')

screen.exitonclick()

