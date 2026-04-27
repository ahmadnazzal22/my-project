from turtle import Screen, Turtle
import time

# --- 1. إعداد الشاشة ---
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game - Classic")
screen.tracer(0) # لإيقاف التحديث التلقائي وجعل الحركة سلسة

# --- 2. فئة المضرب (Paddle) ---
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)

# --- 3. فئة الكرة (Ball) ---
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9 # لزيادة السرعة مع كل صدة

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

# --- 4. تشغيل اللعبة ---
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # التصادم مع الجدران (أعلى وأسفل)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # التصادم مع المضارب
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # خروج الكرة من اليمين (نقطة للمضرب الأيسر)
    if ball.xcor() > 380:
        ball.reset_position()

    # خروج الكرة من اليسار (نقطة للمضرب الأيمن)
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()