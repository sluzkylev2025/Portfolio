from turtle import *

border=Turtle()
border.up()
border.color('steel blue')
border.pensize(5)
border.goto(150,150)
border.pendown()
border.hideturtle()
border.goto(150,-150)
border.goto(-150,-150)
border.goto(-150,150)
border.goto(150,150)

ball=Turtle()
ball.shape('circle')
ball.penup()
ball.color('red')
dx = 3
dy = 2
while True:
  x,y = ball.position()
  if x+dx>=150 or x+dx <= -150:
    dx=-dx
  if y+dy>=150 or y+dy <= -150:
    dy= -dy
  ball.goto(x+dx,y+dy)

