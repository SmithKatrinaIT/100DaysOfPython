import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.car_array = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape='square')
            new_car.shapesize(stretch_wid=1, stretch_len=2) 
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            new_car.goto(300, rand_y)
            self.car_array.append(new_car)
        
    def move_cars(self):
        for car in self.car_array:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT