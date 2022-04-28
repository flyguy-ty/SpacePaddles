# Space Paddles

import turtle
import math

#Create window and background environment
wn = turtle.Screen()
wn.title("Paddle @FlyGuyTy")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score = 0

#Create Objects
# Paddle A
paddle_a = turtle.Turtle() # create object
paddle_a.speed(0) # animation speed (Not moving speed)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("blue")
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle() # create object
paddle_b.speed(0) # animation speed (Not moving speed)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("blue")
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle() # create object
ball.speed(1) # animation speed (Not moving speed)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 1# moves by dx pixels in the x direction
ball.dy = 1 # moves by dy pixels in the y direction

# Planets
red_planet = turtle.Turtle()
red_planet.speed(0)
red_planet.shape("circle")
red_planet.color("red")
red_planet.shapesize(stretch_wid=5, stretch_len=5)
red_planet.penup()
red_planet.goto(100, -600)
red_planet.dx = 0
red_planet.dy = .1

blue_planet = turtle.Turtle()
blue_planet.speed(0)
blue_planet.shape("circle")
blue_planet.color("blue")
blue_planet.shapesize(stretch_wid=5, stretch_len=5)
blue_planet.penup()
blue_planet.goto(-250, -1200)
blue_planet.dx = 0
blue_planet.dy = .1

blue_planet_ring = turtle.Turtle()
blue_planet_ring.speed(0)
blue_planet_ring.shape("square")
blue_planet_ring.color("white")
blue_planet_ring.shapesize(stretch_wid=.25, stretch_len=6)
blue_planet_ring.penup()
blue_planet_ring.goto(-250, -1200)
blue_planet_ring.dx = 0
blue_planet_ring.dy = .1

# Pen
pen = turtle.Turtle() # create object
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.hideturtle()
pen.write("Score {}".format(score), align="center", font=("courier", 24, "normal"))

## Main game loop
#while True:
    #wn.update()
# Functions
# Paddle a moves up
def paddle_a_up():
    if ball.dx < 1:
        y = paddle_a.ycor() #current y-coord of paddle a
        y+= 20
        paddle_a.sety(y)
    else:
        y = paddle_a.ycor()  # current y-coord of paddle a
        y += 30
        paddle_a.sety(y)

# Paddle a moves down
def paddle_a_down():
    if score < 1:
        y = paddle_a.ycor() #current y-coord of paddle a
        y-= 20
        paddle_a.sety(y)
    else:
        y = paddle_a.ycor()  # current y-coord of paddle a
        y -= 30
        paddle_a.sety(y)
# Paddle b moves up
def paddle_b_up():
    if score < 1:
        y = paddle_b.ycor() #current y-coord of paddle b
        y+= 20
        paddle_b.sety(y)
    else:
        y = paddle_b.ycor()  # current y-coord of paddle b
        y += 30
        paddle_b.sety(y)
# Paddle a moves down
def paddle_b_down():
    if score < 1:
        y = paddle_b.ycor() #current y-coord of paddle b
        y-= 20
        paddle_b.sety(y)
    else:
        y = paddle_b.ycor()  # current y-coord of paddle b
        y -= 30
        paddle_b.sety(y)
# Keyboard binding
wn.listen() # Listens for keyboard input
wn.onkeypress(paddle_a_up, "w") #paddle a moves up when user presses w
wn.onkeypress(paddle_a_down, "s") #paddle a moves down when user presses s
wn.onkeypress(paddle_b_up, "Up") #paddle b moves up when user presses w
wn.onkeypress(paddle_b_down, "Down") #paddle b moves down when user presses s

# Main game loop
while True:
    wn.update()
# Moving Objects
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # move the planets
    red_planet.setx(red_planet.xcor() + red_planet.dx)
    red_planet.sety(red_planet.ycor() + red_planet.dy)

    blue_planet.setx(blue_planet.xcor() + blue_planet.dx)
    blue_planet.sety(blue_planet.ycor() + blue_planet.dy)

    blue_planet_ring.setx(blue_planet_ring.xcor() + blue_planet_ring.dx)
    blue_planet_ring.sety(blue_planet_ring.ycor() + blue_planet_ring.dy)

    # Border Checking
    # Ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = .2 #resets horizontal ball speed
        score = 0
        ball.dx = 0.5
        ball.dy = 0.5
        pen.clear()
        pen.write("Score {}".format(score), align="center", font=("courier", 24, "normal"))
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = .2 #resets horizontal ball speed
        score = 0
        ball.dx = 0.5
        ball.dy = 0.5
        pen.clear()
        pen.write("Score {}".format(score), align="center", font=("courier", 24, "normal"))
    # Planets
    if red_planet.ycor() > 590:
        red_planet.sety(-590)

    if blue_planet.ycor() > 590:
        blue_planet.sety(-590)

    if blue_planet_ring.ycor() > 590:
        blue_planet_ring.sety(-590)


    # Colliding with Paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        score += 1
        pen.clear()
        pen.write("Score {}".format(score), align="center", font=("courier", 24, "normal"))
        ball.setx(340)
        if score > 0:
            ball.dx *= -1*(1+0.01*score)
            ball.dy *= 1 * (1 + 0.01 * score)
            print(math.sqrt(ball.dx**2 + ball.dy**2))

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        score += 1
        pen.clear()
        pen.write("Score {}".format(score), align="center", font=("courier", 24, "normal"))
        ball.setx(-340)
        if score > 0:
            ball.dx *= -1 * (1 + 0.05 * score)
            ball.dy *= 1 * (1 + 0.05 * score)
            print(math.sqrt(ball.dx**2 + ball.dy**2))
    if math.sqrt(ball.dx**2 + ball.dy**2) > 1:
        paddle_a.shapesize(stretch_wid=6, stretch_len=1)
        paddle_b.shapesize(stretch_wid=6, stretch_len=1)
    else:
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)