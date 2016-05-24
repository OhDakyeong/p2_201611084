import os
mydir=os.getcwd()
def main_a():
    filename='python.txt'
    myfilename=os.path.join(mydir,filename)
    myfile=open(myfilename,'r')
    try:
        myfile=open(myfilename,'r')
        contents=myfile.readlines()
        for i in range(0,len(contents)):
            if contents[i].find('Python')>=0:
                print contents[i]
            myfile.close()
    except IOError as e:
        print(e)

def main_b():
    myfile2=open('output.txt','w')
    line1='first line\n'
    myfile2.write(line1)
    line2='second line\n'
    myfile2.write(line2)
    line3='third line'
    myfile2.write(line3)
    myfile2.close()
    file2=open('output.txt','r')
    contents2=file2.readlines()
    for i in range(0,len(contents2)):
        if contents2[i].find('line')>=0:
            res=contents2[i].split()
        for n in range(0,len(res)):
            if res[n].find('line')>=0:
                print(res[n].upper())
    file2.close()

def main():
    main_a()
    main_b()

if __name__=="__main__":
    main()