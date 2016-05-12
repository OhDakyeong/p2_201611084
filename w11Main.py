import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.penup()
t2=turtle.Turtle()
t2.penup()
t2.goto(-100,100)
t2.pendown()
t2.fd(200)
def keyup():
    t1.fd(50)
def keydown():
    t1.back(50)
def keyright():
    t1.right(90)
def keyleft():
    t1.left(90)

def mousegoto(x,y):
    t1.setpos(x,y)
    (x,y)=t1.pos() 
    if -100<=x<=100 and y==100:
        t1.write("Mouse Click")

def addkeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keydown, "Down")
    wn.onkey(keyright, "Right")
    wn.onkey(keyleft, "Left")
    
def addmouse():
    wn.onclick(mousegoto)
 
addkeys()
addmouse()
mousegoto(0,0)

wn.listen()
turtle.mainloop()