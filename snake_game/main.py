from turtle import Screen, Turtle
import time
import random

# --- 1. إعدادات الشاشة ---
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - Modern Python")
screen.tracer(0)

# --- 2. فئة الثعبان (Snake Class) ---
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in [(0, 0), (-20, 0), (-40, 0)]:
            self.add_segment(pos)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270: self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90: self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0: self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180: self.head.setheading(0)

# --- 3. فئة الطعام (Food Class) ---
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# --- 4. تشغيل اللعبة ---
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # كشف التصادم مع الطعام
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()

    # كشف التصادم مع الجدران
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False

    # كشف التصادم مع الذيل
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

screen.exitonclick()