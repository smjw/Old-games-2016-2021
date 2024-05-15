import turtle

wn=turtle.Screen()
wn.title("Pong")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
scoreA=0
scoreB=0

#paddle A

paddleA=turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("red")
paddleA.penup()
paddleA.goto(-350,0)

#paddle B

paddleB=turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("blue")
paddleB.penup()
paddleB.goto(350,0)

#ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2

#ball moves insisde main game loop

#writing
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Plaeyr B : 0".format(scoreA,scoreB), align="center", font=("Courier", 24,"normal"))

#paddle a move

def paddleA_up():
    y= paddleA.ycor()
    y+=20
    paddleA.sety(y)

def paddleA_down():
    y= paddleA.ycor()
    y-=20
    paddleA.sety(y)

#paddle b move
    
def paddleB_up():
    y= paddleB.ycor()
    y+=20
    paddleB.sety(y)

def paddleB_down():
    y= paddleB.ycor()
    y-=20
    paddleB.sety(y)

#keyboard bindings
wn.listen()
wn.onkeypress (paddleA_up,"w")
wn.onkeypress (paddleA_down,"s")
wn.onkeypress (paddleB_up,"Up")
wn.onkeypress (paddleB_down,"Down")

#main game loop
while True:
    wn.update()

    #moves ball
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() +ball.dy)

    #border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1#reverses direction of ball

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        scoreA+=1
        pen.clear()
        pen.write("Player A: {} Plaeyr b: {}".format(scoreA,scoreB), align="center", font=("Courier", 24,"normal"))

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        scoreB+=1
        pen.clear()
        pen.write("Player A: {} Plaeyr b: {}".format(scoreA,scoreB), align="center", font=("Courier", 24,"normal"))
#38:44 OF LONG VIDEO FIVE GAME PYTHON !

    #padd;e ball collisions
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddleB.ycor()+40 and ball.ycor()> paddleB.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddleA.ycor()+40 and ball.ycor()> paddleA.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
    
