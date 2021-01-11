from turtle import Turtle
import turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.color("white")
        self.goto(x=0, y=260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))

    def game_over(self):
        turtle.color("white")
        turtle.write("Game Over!", align="center", font=("Arial", 25, "bold"))

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))
