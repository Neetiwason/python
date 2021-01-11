from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake = []
        for position in STARTING_POSITION:
            self.add_part(position)

    def add_part(self, position):
        body_part = Turtle("square")
        body_part.penup()
        body_part.color("#E2F0CB")
        body_part.goto(position)
        self.snake.append(body_part)

    def extend(self):
        self.add_part(self.snake[-1].pos())

    def move(self):
        for part in range(len(self.snake) - 1, 0, -1):
            x = self.snake[part - 1].xcor()
            y = self.snake[part - 1].ycor()
            self.snake[part].goto(x=x, y=y)
        self.snake[0].forward(20)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)
