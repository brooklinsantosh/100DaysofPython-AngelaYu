from turtle import Turtle
import random

class Shape:
    def __init__(self, obj: Turtle)-> None:
        self.obj = obj

    def draw(self, sides: int) -> None:
        self.set_random_color()
        for _ in range(sides):
            self.obj.forward(100)
            self.obj.right(360/sides)

    def random_walk(self, num:int) -> None:
        self.obj.speed("fastest")
        self.obj.penup()
        self.obj.pensize(10)
        self.set_random_starting_point()
        self.obj.pendown()
        for _ in range(num):
            self.set_random_color()
            self.obj.setheading(random.choice([0,90,180,270]))
            self.obj.forward(30)

    
    def set_random_starting_point(self) -> None:
        rand_x = random.randint(-200,200)
        rand_y = random.randint(-200,200)
        self.obj.setposition(rand_x, rand_y)

    def set_random_color(self) -> None:
        colors = ['light gray', 'black', 'medium blue', 'deep sky blue', 'green', 'olive', 'red', 'medium violet red', 'blue violet', 'saddle brown']
        self.obj.color(random.choice(colors))