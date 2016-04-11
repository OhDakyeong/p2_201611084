"""
@author odk
@since 160411
"""

def sumList(aList):
    x=list()
    for i in range(0,aList):
        if i%4==0 and i%5!=0:
            x.append(i)
    mysum=0
    for l in range(0,len(x)):
        mysum=mysum+x[l]
    return mysum

def lab6():
    """programming is really ha ha ha fun"""
    aList=1000
    labsum=sumList(aList)
    print labsum

def main():
    lab6()

if __name__=="__main__":
    main()