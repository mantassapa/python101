import turtle
s = turtle.Screen() 
t = turtle.Turtle()
t.pensize(3)
s.bgcolor('yellow')
t.penup()
t.speed(0)
t.goto(-200, -200)
t.pendown()
t.fd(200)
t.lt(90)
t.fd(400)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(400)

t.penup()
t.goto(-200, -180)
t.lt(90) 
t.pendown()

for h in range(4):
    for j in range(5):
        t.penup()
        t.fd(30)
        t.pendown()
        for i in range (2):
            t.fd(20)
            t.lt(90)
            t.fd(40)
            t.lt(90)
            

        t.end_fill()
    t.penup()
    t.lt(90)
    t.fd(90)
    t.lt(90)
    t.fd(150)
    t.lt(180)
    t.pendown()

t.penup()
t.home()
t.pendown() 
s.exitonclick()