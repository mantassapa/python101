import turtle
s = turtle.Screen() 
t = turtle.Turtle()
s.bgcolor('yellow')
s.title('kontras')
t.pen(pencolor='red', fillcolor='green', pensize=1, speed=9)
t.penup()
t.goto(0,-300)
t.pendown()
colors=['brown', 'blue', 'red', 'green', 'grey', 'crimson', 'coral', 'violet']
t.pencolor(colors[0])
for j in range(3,20):
    for i in range(j):
        t.lt(360/j)
        t.fd(100)
    t.pencolor(colors[j%8])


s.exitonclick()