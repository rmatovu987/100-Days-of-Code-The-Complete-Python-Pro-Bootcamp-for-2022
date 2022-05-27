import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 25:
        food.refresh()
        snake.extend()
        board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 580 or snake.head.xcor() < -580 \
            or snake.head.ycor() > 580 or snake.head.ycor() < -580:
        board.reset()
        snake.reset()

    # Detect collision with tail
    if snake.detect_collision():
        board.reset()
        snake.reset()

screen.exitonclick()
