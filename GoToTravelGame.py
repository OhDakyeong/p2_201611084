import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
img=r"C:\Users\오다경\Mr.gif"
wn.addshape(img)
t1.shape(img)
t1.penup()
t1.goto(0,-200)
bgimg=r"C:\Users\오다경\bg.gif"
wn.bgpic(bgimg)
bgimgR=r"C:\Users\오다경\c1.gif"
bgimgB=r"C:\Users\오다경\c2.gif"
bgimgG=r"C:\Users\오다경\c3.gif"

def keyup():
    t1.setheading(90)
    t1.fd(20)
    Bgturn()
    Exit(t1.pos(),[(-15,150),(15,120)])
    
def keydown():
    t1.setheading(270)
    t1.fd(20)
    Bgturn()
    Exit(t1.pos(),[(-15,150),(15,120)])
    
def keyleft():
    t1.setheading(180)
    t1.fd(20)
    Bgturn()
    Exit(t1.pos(),[(-15,150),(15,120)]) 

def keyright():
    t1.setheading(0)
    t1.fd(20)
    Bgturn()
    Exit(t1.pos(),[(-15,150),(15,120)])
    
def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")
    

t2=turtle.Turtle()

def drawSquareAt(x,y,num):
    t2.penup()
    t2.setpos(x,y)
    t2.pendown()
    for i in range(0,4):
        t2.fd(num)
        t2.right(90)

def TurnR(pos,coord):
    x=pos[0]
    y=pos[1]
    x1=coord[0][0]
    y1=coord[0][1]
    x2=coord[1][0]
    y2=coord[1][1]
    if x1<x<x2 and y2<y<y1:
        t2.clear()
        wn.bgpic(bgimgR)

def TurnB(pos,coord):
    x=pos[0]
    y=pos[1]
    x1=coord[0][0]
    y1=coord[0][1]
    x2=coord[1][0]
    y2=coord[1][1]
    if x1<x<x2 and y2<y<y1:
        t2.clear()
        wn.bgpic(bgimgB)
        
def TurnG(pos,coord):
    x=pos[0]
    y=pos[1]
    x1=coord[0][0]
    y1=coord[0][1]
    x2=coord[1][0]
    y2=coord[1][1]
    if x1<x<x2 and y2<y<y1:
        t2.clear()
        wn.bgpic(bgimgG)
        
def Bgturn():
    TurnR(t1.pos(),[(-300,0),(-220,-80)])
    TurnB(t1.pos(),[(-40,0),(40,-80)])
    TurnG(t1.pos(),[(200,0),(280,-80)])

t2.color("red")
drawSquareAt(-300,0,80)
t2.write("course 1")
t2.color("blue")
drawSquareAt(-40,0,80)
t2.write("course 2")
t2.color("green")
drawSquareAt(200,0,80)
t2.write("course 3")

t3=turtle.Turtle()
t3.penup()
t3.goto(-15,150)
t3.pendown()
for i in range(0,4):
    t3.fd(30)
    t3.right(90)
t3.write("Go to HOME, Bye")

def Exit(pos,coord):
    x=pos[0]
    y=pos[1]
    x1=coord[0][0]
    y1=coord[0][1]
    x2=coord[1][0]
    y2=coord[1][1]
    if x1<x<x2 and y2<y<y1:
        wn.bye()


addkeys()
wn.listen()
turtle.mainloop()