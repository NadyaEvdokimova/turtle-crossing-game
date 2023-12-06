import turtle
from turtle import Turtle
import random
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
turtle.colormode(255)


def color_choice():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.color(color_choice())
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.current_speed)

    def cars_speed_up(self):
        self.current_speed += MOVE_INCREMENT



