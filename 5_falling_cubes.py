"Try to Caught falling cubes by pushing them before cross red line"
from turtle import *
from random import randint
from time import sleep

t1 = Turtle()
t1.color('steel blue')
t1.shape('square')
t1.left(-90)
t1.hideturtle()

t2 = Turtle()
t2.color('green')
t2.shape('square')
t2.left(-90)
t1.penup()
t2.penup()

t2.hideturtle()
border = Turtle()
border.color('red')
border.penup()
border.goto(-150, -150)
border.pendown()
border.hideturtle()
border.goto(150, -150)


def start1():
    t1.hideturtle()
    t2.hideturtle()
    t1.goto(randint(-150, 150), randint(0, 170))
    t2.goto(randint(-150, 150), randint(0, 170))
    t1.showturtle()
    t2.showturtle()
    move1()


def move1():
    while t1.ycor() > -140 and t2.ycor() > -140:
        t1.speed(randint(2, 6))
        t1.fd(10)
        sleep(0.5)
        t2.speed(randint(2, 6))
        t2.fd(10)
        sleep(0.5)
    else:
        t1.write('Проигрыш')
        t1.hideturtle()
        t2.hideturtle()


def catch1(x, y):
    start1()


def catch2(x, y):
    start1()


t1.onclick(catch1)
t2.onclick(catch2)
start1()
