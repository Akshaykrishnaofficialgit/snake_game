from turtle import Turtle
snakepos = [(0, 0), (-20, 0), (-40, 0)]
MOVE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_seg=[]
        self.create_snake()
        self.hideturtle()
    def create_snake(self):
        for i in snakepos:
            self.add_seg(i)

    def add_seg(self, i):
        snake_body = Turtle(shape="square")
        snake_body.penup()
        snake_body.color("green")
        snake_body.goto(i)
        self.snake_seg.append(snake_body)

    def extend(self):
        self.add_seg(self.snake_seg[-1].position())

    def move(self):
        for i in range(len(self.snake_seg) - 1, 0, -1):
            new_x = self.snake_seg[i - 1].xcor()
            new_y = self.snake_seg[i - 1].ycor()
            self.snake_seg[i].goto(new_x, new_y)
        self.snake_seg[0].forward(MOVE)
    def up(self):
        if self.snake_seg[0].heading() != DOWN:
            self.snake_seg[0].setheading(90)
    def down(self):
        if self.snake_seg[0].heading() != UP:
            self.snake_seg[0].setheading(270)
    def left(self):
        if self.snake_seg[0].heading() != RIGHT:
            self.snake_seg[0].setheading(180)
    def right(self):
        if self.snake_seg[0].heading() != LEFT:
            self.snake_seg[0].setheading(0)