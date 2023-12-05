# simple pong game in python 
import turtle
import time

wn = turtle.Screen()
wn.title("Pong")

wn.bgcolor("black")

wn.setup(width=800, height=600)

wn.tracer(0) # stops the window from updating ... helps running game faster

# Score
scoreA = 0
scoreB = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx = 1
ball.dy = 1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: {scoreA} Player B: {scoreB}", align="center", font=("Courier", 24, "normal"))

## Functions 

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y < 280:
        paddle_a.sety(y)
    

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y > -280:
        paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y < 280:
        paddle_b.sety(y)
    

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y > -280:
        paddle_b.sety(y)

## Keyboard Bindings (
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


##* Main game loop

counter = turtle.Turtle()
counter.speed()
counter.color("white")
counter.penup()
counter.hideturtle()
counter.goto(0,0)
counter.write("3",align="center", font=("Courier", 48, "normal") )
wn.update()
time.sleep(1)
counter.clear()
counter.write("2",align="center", font=("Courier", 48, "normal") )
wn.update()
time.sleep(1)
counter.clear()
counter.write("1",align="center", font=("Courier", 48, "normal") )
wn.update()
time.sleep(0.5)
counter.clear()

while True:
    wn.update();
    pen.clear()
    pen.write(f"Player A: {scoreA} Player B: {scoreB}", align="center", font=("Courier", 24, "normal"))

    
    ## move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    ## bounce the ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        time.sleep(0.8)
        ball.dx *= -1
        scoreA += 1

        
    if ball.xcor() < -390:
        ball.goto(0,0)
        time.sleep(0.8)
        ball.dx *= -1
        scoreB += 1
        
    ## Collision 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
     
