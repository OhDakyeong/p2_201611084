def lab6_3():
    min=1
    max=10
    import random
    set=random.randrange(min,max)
    num=max/2
    check=1
    ment="You got the answer at"
    if num==set:
        print "It is",set
        print ment,check
    elif num<set:
        print "The Number is Higher than 5"
        if set==(num+3):
            check=check+1
            print "It is",set
            print ment,check
        elif set>(num+3):
            check=check+2
            print"The Number is Higher than 8"
            if set==(num+4):
                print "It is",set
                print ment,check
            else:
                check=check+3
                print "The Number is Higher than 9"
                print "It is",set
                print ment,check
        else:
            print "The Number is Lower than 8"
            if set==(num+2):
                check=check+2
                print "It is",set
                print ment,check
            elif set<(num+2):
                check=check+3
                print "The Number is Lower than 7"
                print "It is",set
                print ment,check
    elif num>set:
        print "The Number is Lower than 5"
        if set==(num-2):
            check=check+1
            print "It is",set
            print ment,check
        elif set>(num-2):
            print "The Number is Higher than 3"
            check=check+2
            print "It is",set
            print ment,check
        else:
            print "The Number is Lower than 3"
            if set==(num-3):
                check=check+2
                print "It is",set
                print ment,check

            else:
                check=check+3
                print "The Number is Lower than 2"
                print "It is",set
                print ment,check
lab6_3()