def bow():
    class Dog(object):
        def __init__(self,name):
            self.name=name
        def getName(self):
            print("my dog name is ",self.name)
        def talk(self):
            print("mung mung")
        
    class ShihTzu(object):
        def talk(self):
            print("si si")
        
    class Maltese(object):
        def talk(self):
            print("mal mal")

    mydog=Dog('poppy')
    mydog.talk()
    shihtzu=ShihTzu()
    shihtzu.talk()
    maltese=Maltese()
    maltese.talk()

def lab14_2():
    bow()

def main():
    lab14_2()

if __name__="__main__":
    main()