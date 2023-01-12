import turtle
from turtle import Turtle, Screen
import random

my_screen = Screen()
turtle.colormode(255)

color_list = [(224, 221, 183), (208, 240, 143), (136, 110, 107), (83, 175, 143), (146, 75, 124), (29, 106, 164), (227, 158, 66), (231, 214, 93), (188, 42, 84), (219, 139, 173), (139, 105, 59)]

tummy = turtle.Turtle()
tummy.speed('fastest')


for a in range(1, 361, 5):
    tummy.color(random.choice(color_list))
    tummy.circle(100)
    tummy.setheading(a)

my_screen.exitonclick()