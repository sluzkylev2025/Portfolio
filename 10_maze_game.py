from turtle import *
from random import randint

tsize = 20
s_width = 200
s_height = 180

# === КЛАССЫ ===

class Rock(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('gray')
        self.shape('circle')
        self.speed(0)
        self.falling = False
        self.step = 5

    def drop(self, x):
        self.goto(x, 180)
        self.showturtle()
        self.falling = True

    def fall_step(self):
        if self.falling:
            self.sety(self.ycor() - self.step)
            if self.ycor() < -180:
                self.hideturtle()
                self.falling = False

class Sprite(Turtle):
    def __init__(self, x, y, color):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape('turtle')
        self.step = 10
        self.points = 0

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
        for wall in walls:
            if wall.is_collision(self):
                self.goto(self.xcor(), self.ycor() - self.step)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
        for wall in walls:
            if wall.is_collision(self):
                self.goto(self.xcor(), self.ycor() + self.step)

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
        for wall in walls:
            if wall.is_collision(self):
                self.goto(self.xcor() + self.step, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())
        for wall in walls:
            if wall.is_collision(self):
                self.goto(self.xcor() - self.step, self.ycor())

    def is_collide(self, sprite):
        return self.distance(sprite.xcor(), sprite.ycor()) < 30


class Wall(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.shape('square')
        self.color('ghost white')
        self.width = 40
        self.height = 40

    def is_collision(self, other):
        return (
            (self.xcor() + self.width / 2) > other.xcor() - 10 and
            (self.xcor() - self.width / 2) < other.xcor() + 10 and
            (self.ycor() + self.height / 2) > other.ycor() - 10 and
            (self.ycor() - self.height / 2) < other.ycor() + 10
        )


class Arrow(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.penup()
        self.speed(3)
        self.goto(x, y)
        self.color('red')
        self.shape('arrow')
        self.step = 5
        self.width = 20
        self.height = 20

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

# === ЭКРАН И НАСТРОЙКА ===

scr = Screen()
scr.bgcolor('dark slate blue')
scr.tracer(0)  # Отключаем анимацию до полной отрисовки

walls = []

# === СОЗДАНИЕ СТЕН ===

# Вертикальная соединяющая стена
for i in range(-70, 71, 15):
    walls.append(Wall(-200, i))

# Горизонтальные стены
for i in range(-200, 0, 15):
    walls.append(Wall(i, 70))
    walls.append(Wall(i, -70))

for i in range(-70, 0, 15):
    walls.append(Wall(-100, i))

for i in range(0, 100, 15):
    walls.append(Wall(i, 0))
    walls.append(Wall(i, -150))

for i in range(-150, 0, 15):
    walls.append(Wall(0, i))

for i in range(0, 150, 15):
    walls.append(Wall(i, 140))

for i in range(10, 140, 15):
    walls.append(Wall(90, i))

# Рамка по периметру
for x in range(-200, 201, 20):
    walls.append(Wall(x, -200))
    walls.append(Wall(x, 200))
for y in range(-180, 181, 20):
    walls.append(Wall(-200, y))
    walls.append(Wall(200, y))

scr.update()  # Показываем всё после создания

# === ИГРОКИ И ПРЕПЯТСТВИЯ ===

player = Sprite(-150, -30, 'powder blue')
player2 = Sprite(-70, -110, 'red')
rock = Rock()

ob1 = Arrow(-180, 110)
ob1.set_move(-180, 110, 180, 110)

ob2 = Arrow(170, -140)
ob2.set_move(170, -140, -170, -140)

ob3 = Arrow(-50, -150)
ob3.set_move(-50, -150, -50, 150)

# === УПРАВЛЕНИЕ ===

scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')

# === СЛУЧАЙНОЕ ПАДЕНИЕ КАМНЯ ===

def random_drop():
    if not rock.falling:
        rock.drop(randint(-180, 180))
    scr.ontimer(random_drop, randint(3000, 7000))

# === ИГРОВОЙ ЦИКЛ ===

def game_loop():
    ob1.make_step()
    ob2.make_step()
    ob3.make_step()
    rock.fall_step()

    if player.is_collide(ob1) or player.is_collide(ob2) or player.is_collide(ob3) or player.is_collide(rock):
        player.write('Ты проиграл', align='center', font=('Arial', 14, 'bold'))
        return

    if player.is_collide(player2):
        ob1.hideturtle()
        ob2.hideturtle()
        ob3.hideturtle()
        rock.hideturtle()
        player.write('Ты выиграл', align='center', font=('Arial', 14, 'bold'))
        player2.color('powder blue')
        return

    scr.update()
    scr.ontimer(game_loop, 30)

# === СТАРТ ===

random_drop()
game_loop()
scr.mainloop()
