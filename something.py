import turtle
t=turtle.Turtle()

def square(x,y,l):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x+l,y)
    t.goto(x+l,y+l)
    t.goto(x,y+l)
    t.goto(x,y)

    if l>10:
        square(x+l,y+l,l/2)

square(0,0,100)
turtle.mainloop()