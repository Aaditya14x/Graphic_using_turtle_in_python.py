from turtle import *
from random import randint
speed(0)
bgcolor("black")
X = 1
while X < 400:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    fd(50+X)
    rt(90.911)
    X += 1
    exitonclick