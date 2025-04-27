from turtle import Turtle


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed(0)
        
    def draw_divider(self, length, dash_length=10):
        self.penup()
        self.goto(0, -300)
        self.left(90)
        self.shapesize(stretch_wid=2, stretch_len=2)
        for i in range(0, length, dash_length * 2):
            self.pendown()
            self.forward(dash_length)
            self.penup()
            self.forward(dash_length)
        
        