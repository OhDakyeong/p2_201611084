def saveTracks():
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    mytracks=list()
    t1.speed(1)
    t1.penup()
    t1.goto(-400,300)
    mytracks.append(t1.pos())
    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(250)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.fd(150)
    mytracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(400)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.fd(200)
    mytracks.append(t1.pos())
    wn.exitonclick()
    return mytracks

def replayTracks(mytracks):
    for t in mytracks:
        print t
    
def lab7_2():
    mytracks=saveTracks()
    replayTracks(mytracks)
    
def main():
    lab7_2()
 
if __name__=="__main__": 
    main() 
