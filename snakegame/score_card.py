from turtle import Turtle
ALIGNMENT="center"
FONT=("courier", 18, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_score.txt") as snake_score:
            self.highscore=snake_score.read()
        self.penup()
        self.goto(0,270)
        self.color("yellow")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.score}  HighScore:{self.highscore}", align=ALIGNMENT, font=FONT)

    def collison(self):
        self.clear()
        self.goto(0,0)
        self.hideturtle()
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def increase_highscore(self):
        if self.score>int(self.highscore):
            self.highscore=self.score
            with open("snake_score.txt","w") as snake_score:
                snake_score.write(str(self.highscore))
        else:
            pass
        self.clear()
        self.update_score()