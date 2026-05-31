from turtle import *
from random import randint
from time import sleep

finish = 200


def dance(t):
    t.showturtle()
    t.speed(15)
    t.goto(-20, 50)
    t.write('Win', font=('Arial', 16, 'bold'))
    t.goto(30, 60)
    t.stamp()
    t.penup()
    t.goto(0, -60)
    for i in range(20):
        t.fd(30)
        t.stamp()
        t.left(360 / 20)
    t.goto(-40, 0)
    t.pendown()
    t.color('yellow')
    for i in range(3):
        t.begin_fill()
        for i in range(5):
            t.fd(30)
            t.left(144)
        t.end_fill()
        t.penup()
        t.fd(40)
        t.pendown()

    t.hideturtle()


class Turtle_drive(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape('turtle')
        self.color(color)


def wall():
    speed(10)
    penup()
    color('red')
    pensize(5)
    goto(-160, 90)
    pendown()
    goto(-160, -90)
    penup()
    goto(190, 90)
    pendown()
    goto(190, -90)
    hideturtle()


wall()
t1 = Turtle_drive(-170, 40, 'steel blue')
t2 = Turtle_drive(-170, -40, 'pink')
t3 = Turtle_drive(-170, 0, 'green')
t4 = Turtle_drive(-170, -80, 'purple')

sleep(1)

while t1.xcor() < finish and t2.xcor() < finish and t3.xcor() < finish and t4.xcor() < finish:
    t1.forward(randint(1, 10))
    t2.forward(randint(1, 10))
    t3.forward(randint(1, 10))
    t4.forward(randint(1, 10))
sleep(1)


clear()
max_x = max(t1.xcor(), t2.xcor(), t3.xcor(), t4.xcor())
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t4.hideturtle()
if t1.xcor() == max_x:
    dance(t1)
if t2.xcor() == max_x:
    dance(t2)
if t3.xcor() == max_x:
    dance(t3)
if t4.xcor() == max_x:
    dance(t4)

