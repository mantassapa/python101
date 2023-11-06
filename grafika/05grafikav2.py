import turtle
s = turtle.Screen() 
t = turtle.Turtle()
s.bgcolor('yellow')
s.title('kontras')
t.pen(pencolor='red', fillcolor='green', pensize=3, speed=9)
t.penup()
t.goto(0,-300)
t.pendown()
colors=['brown', 'blue', 'red', 'green', 'grey', 'crimson', 'coral', 'violet']
t.pencolor(colors[0])
for j in range(20,2,-1):
    t.fillcolor(colors[(j+1)%8])
    t.begin_fill()
    for i in range(j):
        t.lt(360/j)
        t.fd(100)  
    t.end_fill()
    t.pencolor(colors[j%8])


s.exitonclick()