import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Step 1: set up screen 
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Step 2: create a player
player = Player()

#Step 3: listen to up arrow key
screen.listen()
screen.onkey(player.up, 'Up')

#Step 4: create car
car_manager = CarManager()

#Step 5: create scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.generate_car()
    car_manager.move_cars()
    

    #detect player reaches top of the screen
    if player.ycor() > 555:
        player.starting_position()
        
    #detect collision with car
    for car in car_manager.car_array:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    #Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
            
            


screen.exitonclick()