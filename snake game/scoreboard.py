from turtle import Turtle


def read_high_score():
    with open(file='data.txt') as file:
        return file.read()


def write_high_score(value: int):
    with open(file='data.txt', mode='w') as file:
        file.write(str(value))


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = int(read_high_score())
        self.color('white')
        self.penup()
        self.goto(0, 500)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} | High Score: {self.high_score}', align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER', align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        write_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()
