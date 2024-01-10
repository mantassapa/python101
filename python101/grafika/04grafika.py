import turtle
s = turtle.Screen() 
t = turtle.Turtle()
t.speed(8)
s.bgcolor('yellow')
s.title('Hello world')

t.pen(pencolor='red', fillcolor='silver', pensize=1, speed=9)

t.begin_fill()

for i in range(5):
    t.lt(72)
    t.fd(100)

t.end_fill()

t.reset()


s.exitonclick()