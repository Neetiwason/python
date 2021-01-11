from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to snake world!")
screen.tracer(0)
screen.bgcolor("#FFB7B2")
# TODO: CREATE A SNAKE
snake = Snake()
# TODO: create food
food = Food()
# TODO: CREATE A SCOREBOARD
score = ScoreBoard()

# TODO: control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO: MOVE A SNAKE
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO: detect collision with food
    if snake.snake[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.refresh()

    # TODO: detect collision with wall
    if -280 > snake.snake[0].xcor() or snake.snake[0].xcor() > 280 or -280 > snake.snake[0].ycor() or snake.snake[
        0].ycor() > 280:
        score.game_over()
        game_on = False

    # TODO: detect collision of snake head with its body parts
    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
