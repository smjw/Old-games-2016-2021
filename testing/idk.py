import turtle
from tkinter import *

wn=turtle.Screen()
wn.title("game")
wn.bgcolor("white")
wn.setup(width=800,height=600)
wn.tracer(0)

self=turtle.Turtle()
self.speed(0)
self.shape("square")
self.color("blue")
self.penup()
self.goto(-350,0)

self2=turtle.Turtle()
self2.speed(0)
self2.shape("square")
self2.color("red")
self2.penup()
self2.goto(-350,0)

apple=turtle.Turtle()
apple.shape("square")
apple.color("green")
apple.penup()
apple.goto(55,55)

#updown
def self_up():
    y= self.ycor()
    y+=20
    self.sety(y)

def self_down():
    y= self.ycor()
    y-=20
    self.sety(y)

#rightleft
def self_right():
    x=self.xcor()
    x+=20
    self.setx(x)

def self_left():
    x=self.xcor()
    x-=20
    self.setx(x)
    
#2updowon
def self2_up():
    y= self2.ycor()
    y+=20
    self2.sety(y)

def self2_down():
    y= self2.ycor()
    y-=20
    self2.sety(y)

#2rightleft
def self2_right():
    x=self2.xcor()
    x+=20
    self2.setx(x)

def self2_left():
    x=self2.xcor()
    x-=20
    self2.setx(x)

#places apple on screen



    
wn.listen()
wn.onkeypress (self_up,"w")
wn.onkeypress (self_down,"s")
wn.onkeypress (self_right,"d")
wn.onkeypress (self_left,"a")
wn.onkeypress (self2_up,"Up")
wn.onkeypress (self2_down,"Down")
wn.onkeypress (self2_right, "Right")
wn.onkeypress (self2_left, "Left")

while True:
    wn.update()

    
