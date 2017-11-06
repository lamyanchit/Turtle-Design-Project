import turtle
from myFunctionfile import*
bob=turtle.Turtle()
turtle.colormode(255)
turtle.bgcolor(0,0,0)
from random import*
s=randint(3,8)
bob.speed(11)

for times in range(20):
    r=randint(100,255)
    g=randint(100,255)
    b=randint(100,255)
    c=(r,g,b)
    bob.color(c)
    sides=randint(3,8)
    distance=randint(20,100)
    x=randint(-600,600)
    y=randint(-600,600)
    jump(bob,x,y)
    polygon(bob,sides,distance)
    
bob.penup()
bob.goto(0,0)
bob.pendown()
for times in range(100):
    c=(50,50,90)
    bob.color(c)
    bob.circle(101-times)
    bob.right(55)
    draw_star(bob,times,144)

for times in range(100):
    bob.color(168,55,64)
    bob.circle(times)
    bob.right(55)
    draw_star(bob,101-times,144)

for times in range(50):
    bob.color(80,160,170)
    bob.circle(51-times)
    bob.right(60)
    draw_star(bob,times,144)







