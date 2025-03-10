# Auteur : Ibrahima Oumar LY
# Date de création : 2025-03-03
# Description : Ce fichier contient les fonctions pour le jeu Snake.

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


def read_high_score():
    with open("data.txt") as f_score:
        return int(f_score.read())


def write_high_score(score):
    with open("data.txt", mode="w") as f_score:
        f_score.write(f"{score}")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(read_high_score())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            write_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
