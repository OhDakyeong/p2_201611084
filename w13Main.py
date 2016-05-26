import time
def Number():
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

def Line():
    t1=open('output.txt','w')
    t1.write('frist line\n second line\n third')
    t1.close()
    fin=open('output.txt','r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        for word in words:
            if word=='line':
                word=word.upper()
                fout.write(word+'\n')
            else:
                fout.write(word+' ')
    fin.close()
    fout.close()

def lab13():
    Number()
    Line()

def main():
    lab13()

if __name__=="__main()__":
    main()