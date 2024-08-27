from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.shapesize(stretch_wid=0.7,stretch_len=0.7)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-370, 370)
        y_cor = random.randint(-270, 250)
        self.goto(x_cor, y_cor)