userA=raw_input("get userA choice: ")
userB=raw_input("get userB choice: ")
print userA, userB
def GameRSP(userA,userB):
    if userA==userB:
        print ("draw")
    elif userA=="r" and userB=="s" or userA=="s" and userB=="p" or userA=="p" and userB=="r":
        print("userA wins")
    elif userA=="s" and userB=="r" or userA=="p" and userB=="s" or userA=="r" and userB=="p":
        print("userB wins")
    else:
        print ("Please check your choice.")
GameRSP(userA,userB)

