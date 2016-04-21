import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.penup()
t1.goto(-120,250)
t1.write("Move your Turtle to get points!")
def Figure(size,sides,angle,set):
    sides=int(sides)
    t1.penup()
    t1.goto(set)
    t1.pendown()
    for i in range(0,sides):
        t1.fd(size)
        t1.right(angle)
Figure(100,3,120,(-350,200))
t1.write("Move to center then you get 5 points")
Figure(80,4,90,(-140,200))
t1.write("Move to center then you get 4 points")
Figure(130,5,144,(60,200))
t1.write("Move to center then you get 6 points")
Figure(70,5,72,(-230,60))
t1.write("Move to center then you get 3 points")
Figure(60,6,60,(50,60))
t1.write("Move to center then you get 2 points")
t1.penup()
t1.goto(0,-200)
t1.pendown()
t1.circle(20)
t1.penup()
t1.goto(0,-220)
t1.write("START")
t1.goto(-200,-200)
t1.write("Point : ")
t1.goto(-160,-200)
t2=turtle.Turtle()
t2.shape("turtle")
t2.penup()
t2.goto(0,-180)
(x,y)=t2.pos()
def k1():
     t2.forward(10)
     if (-320<=x<=-280 and 130<=y<=175):
          score=score+5
          t1.write(score)
	  print "your score is %d "% score
          t1.goto(0,180)
def k2():
     t2.back(10)
def k3():
     t2.left(15)
def k4():
     t2.right(15)
global score
score=0
wn.onkey(k1,"Up")
wn.onkey(k2,"Down")
wn.onkey(k3,"Left")
wn.onkey(k4,"Right")
wn.listen()
wn.exitonclick()