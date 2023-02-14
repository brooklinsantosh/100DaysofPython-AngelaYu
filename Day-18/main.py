from turtle import Turtle, Screen
from shapes import Shape

tim = Turtle()
screen = Screen()
screen.screensize(200,200)
tim.shape("turtle")
tim.color("red")

s = Shape(tim)
# for i in range(3, 11):
#     s.draw(i)

s.random_walk(200)






screen.exitonclick()

