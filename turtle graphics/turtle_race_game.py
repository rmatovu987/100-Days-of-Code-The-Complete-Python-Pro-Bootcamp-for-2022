import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(3000, 1500)
colors = ['red', 'blue', 'orange', 'purple', 'green', 'yellow']
all_turtles = []

bet = screen.textinput('Make your bet', 'Which turtle will win the race? Enter a color: ')

y = -300
for tur in range(0, 6):
    red = Turtle('turtle')
    red.color(colors[tur])
    red.penup()
    red.goto(-1490, y)
    y += 100
    all_turtles.append(red)

if bet:
    is_race_on = True

while is_race_on:
    for tur in all_turtles:
        if tur.xcor() > 1460:
            is_race_on = False
            if bet.lower() == tur.color()[0]:
                print(f"You've won! {tur.color()[0]} turtle is the winner")
            else:
                print(f"You've lost! {tur.color()[0]} turtle is the winner")
        rand_dist = random.randint(0, 10)
        tur.forward(rand_dist)

screen.exitonclick()
