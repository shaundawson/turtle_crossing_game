from turtle import Turtle 
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_CARS = 150




# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. 
class CarManager:
    def __init__(self):
        self.all_cars = []
        self.cars_speed = 0.1


    def create_car(self):
        random_chance = random.randint(1, 20)
        if random_chance == 20:
            new_car = Turtle()
            new_car.shape("square")
            new_car.speed("fastest")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_position = random.randint(-250, 250)
            new_car.goto(300, y_position)
            self.all_cars.append(new_car)

    
    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.cars_speed *= 0.9
       





