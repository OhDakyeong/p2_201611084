import os
mydir=os.getcwd()

def text():
    data=[1,2,3,4,5,6,7,8,9,10]
    num=open('ouputNumber.txt','w')
    for i in data:
        if i%2==0:
            i=str(i)
            num.write(i+'\n')
        else:
            i=str(i)
            num.write(i+'\t')
    num.close()

def drawRectangle():
    myfile=open('rectangle.txt','w')
    myfile.write('0,0,100,100'+'\n')
    myfile.write('200,200,150,150'+'\n')
    myfile.close()

def getRectangle():
    rec=open('rectangle.txt')
    coords=[]
    for line in rec:
        line1=line.split(',')
        x1=int(line1[0])
        y1=int(line1[1])
        x2=int(line1[2])
        y2=int(line1[3].strip())
        coords.append([(x1,y1),(x2,y2)])
    rec.close()

def drawSquare(coords):
    x=list()
    y=list()
    for coord in coords:
        x.append(coord[0][0])
        x.append(coord[1][0])
        y.append(coord[0][1])
        y.append(coord[1][1])
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.goto(x[0],y[0])
    t1.goto(x[0],y[1])
    t1.goto(x[1],y[1])
    t1.goto(x[1],y[0])
    t1.goto(x[0],y[0])
    t1.penup()
    t1.goto(x[2],y[2])
    t1.pendown()
    t1.goto(x[2],y[3])
    t1.goto(x[3],y[3])
    t1.goto(x[3],y[2])
    t1.goto(x[2],y[2])
    wn.exitonclick()

def mfile():
    filename='myfile.txt'
    myfilename=os.path.join(mydir,filename)
    filename2='ouputNumber.txt'
    myfilename2=os.path.join(mydir,filename2)
    fin1=open(myfilename,'a')
    fin2=open(myfilename2,'r')
    for line in fin2:
        fin1.write(line)
    fin1.close()
    fin2.close()

def lab14():
    txt()
    mfile()
    num=drawRectangle()
    coords=getRectangle()
    drawSquare(coords)
    

def main():
    lab14()

if __name__=="__main()__":
    main()