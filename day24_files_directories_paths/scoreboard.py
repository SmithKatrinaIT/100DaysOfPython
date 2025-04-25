from turtle import Turtle

# class constants
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
SCORE_COLOR = "white"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
       
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        
    def get_high_score(self):
        with open('data.txt') as file:
            self.high_score = file.read()
    

    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def reset(self):
        
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()
        

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)

