import turtle
s = turtle.Screen() 
t = turtle.Turtle()
t.speed(8)
s.bgcolor('yellow')
s.title('Hello world')
t.pensize(5)
t.pencolor('red')

for i in range(5):
    t.lt(72)
    t.fd(100)

t.penup()
t.goto(150,150)
# t.fd(100)
t.pendown()
t.fillcolor('blue')
t.begin_fill()

for i in range(5):
    t.lt(72)
    t.fd(100)
t.end_fill()

s.exitonclick()