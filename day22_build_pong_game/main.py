from turtle import Screen
from paddle import Paddle
from ball import Ball
from divider import Divider
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350,0))
ball = Ball()
divider = Divider()
divider.draw_divider(650, 20)

# listen to keyboard commands
screen.listen()

# set which keys will control the paddle
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


# with tracer(0) set to zero animation; we have to update the screen everytime with a loop of some kind
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    
    #detect collison with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
screen.exitonclick()

