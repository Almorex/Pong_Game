import turtle #to draw graphics

wn = turtle.Screen()

canvas = wn.getcanvas()
root = canvas.winfo_toplevel()

wn.title("PONG @almorex")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()#small t bcuz it is module name and capital t bcuz it is class name
paddle_a.speed(0)#speed of animation not for paddle
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)#by default size is 20px 20px, in this we made 5 times it was before that is 100px 20px
paddle_a.penup()#turtle draws line when it goes to avoid that
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_a.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.35
ball.dy = 0.35

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center" ,font=("Courier", 24, "bold"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y = y+20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y = y-20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y = y+20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y = y-20
    paddle_b.sety(y)

#  Keyboard binding
wn.listen()# tells the program for keyboard input
wn.onkeypress(paddle_a_up, "w")# tells the program when user enters w move up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game
while True:
    wn.update() #update the screen whenver game runs

    #the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #ball.setx(ball.xcor() + ball.dx )

# BORDER CHECKING
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # To reverse the direction of ball
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
#COLLISON
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50  ):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50  ):
        ball.setx(-340)
        ball.dx *= -1
