from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_card import Score
import time

# Set up the screen
my_screen = Screen()
my_screen.tracer(0)
my_screen.setup(height=600, width=800)
my_screen.bgcolor("black")
my_screen.title("Snake game")

# Create snake, food, and score objects
My_snake = Snake()
snake_food = Food()
the_score = Score()

# Start the game loop
game_is_on = True
my_screen.listen()
my_screen.onkey(My_snake.up, "Up")
my_screen.onkey(My_snake.down, "Down")
my_screen.onkey(My_snake.left, "Left")
my_screen.onkey(My_snake.right, "Right")

while game_is_on:
    my_screen.update()
    time.sleep(0.10)
    My_snake.move()
    if My_snake.snake_seg[0].distance(snake_food) < 15:
        My_snake.extend()
        snake_food.refresh()
        the_score.increase_score()
        the_score.increase_highscore()
    if My_snake.snake_seg[0].xcor() > 380 or My_snake.snake_seg[0].xcor() < -380 or My_snake.snake_seg[0].ycor() > 300 or My_snake.snake_seg[0].ycor() < -290:
        game_is_on = False
        the_score.collison()
        my_screen.bgcolor("red")
    for segment in My_snake.snake_seg[1:]:
        if My_snake.snake_seg[0].distance(segment) < 10:
            game_is_on = False
            the_score.collison()
            my_screen.bgcolor("red")






























my_screen.exitonclick()