def drawSquareAtSave(size, pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks

def drawSquareFrom():
    p=list()
    p=((0,0),(80,0),(80,80),(0,80),(0,0))
    for i in range(0,5):
        t1.goto(p[i])
    return p

def lab7_b():
    mytrack=drawSquareAtSave(size,pos)
    print mytrack
    
def lab7_c():
    mytrack2=drawSquareFrom()
    print mytrack2
    
def main():
    lab7_b()
    lab7_c()
    
if _name_=="_main_": 
    main() 
