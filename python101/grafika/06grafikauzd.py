import turtle
s = turtle.Screen() 
t = turtle.Turtle()
colors=['brown', 'blue', 'red', 'green', 'grey', 'crimson', 'coral', 'violet']
t.pencolor(colors[0])
t.pensize(3)
t.penup()
t.goto(-400,0)
t.pendown()
for j in range(5):
    for i in range (4):
        t.fd(100)
        t.lt(90)
    t.penup()
    t.fd(150)   
    t.pendown()
    t.pencolor(colors[(j+1)%8])
t.penup()
t.home()
t.pendown() 
s.exitonclick()