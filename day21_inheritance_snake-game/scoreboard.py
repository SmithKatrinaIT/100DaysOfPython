from turtle import Turtle

# class constants
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
SCORE_COLOR = "white"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Scoreboard: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)

