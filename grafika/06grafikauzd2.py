import turtle
s = turtle.Screen() 
t = turtle.Turtle()
colors=['brown', 'blue', 'red', 'green', 'grey', 'crimson', 'coral', 'violet']
t.pencolor(colors[0])
t.pensize(3)
s.bgcolor('yellow')
for j in range(6):
    t.fillcolor(colors[(j+1)%8])
    t.begin_fill()
    for i in range (6):
        t.fd(100)
        t.lt(60)
    t.end_fill()
    t.penup()
    t.fd(100)
    t.rt(60)   
    t.pendown()
    t.pencolor(colors[(j+1)%8])
t.penup()
t.home()
t.pendown() 
s.exitonclick()