word="sangmyung university"
wd="7 hongjidong"
my=set(['TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'])
friend=set(['coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'])


def charCount(word):
    import matplotlib
    import matplotlib.pyplot as plt
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    print d
    plt.bar(range(0,len(d)),d.values(),align='center')
    plt.xticks(range(0,len(d)),list(d.keys())
    plt.show()

def countDigitsLetters(wd):
    import matplotlib
    import matplotlib.pyplot as plt
    d={"word":0, "num":0}
    for c in wd:
        if c.isdigit()==True:
            d["num"]+=1
        elif c.isalpha()==True:
            d["word"]+=1
    print d
    plt.bar(range(0,len(d)),d.values(), align='center')
    plt.xticks(range(0,len(d)),list(d.keys()))
    plt.show()

def Home():
    print "my home: ",my
    print "friend's home: ", friend
    print "ONLY my home: ",my.difference(friend)
    print "ONLY friend's home: ",friend.difference(my)
    print "BOTH: ",my.intersection(friend)
    print "all: ", my.union(friend)
    print "Everything: ", len(my.union(friend))

def lab8_a():
    charCount()

def lab8_b():
    countDigitsLetters()

def lab8_c():
    Home()

def main():
    lab8_a()
    lab8_b()
    lab8_c()

if _name_=="_main_":
    main()


