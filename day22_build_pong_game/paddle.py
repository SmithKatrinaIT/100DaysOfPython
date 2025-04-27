from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        
        # by default a turle object size is 20 x 20
        # in order for the "paddle" to by 100px x 20px, we use the shapesize method to set stretch_wid to 5 x 20 = 100
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        
    def create_paddle():
        pass
       
    def move(self):
        pass
    
    
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
            
        

