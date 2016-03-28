temp=raw_input("user input temperature: ")

sel=raw_input("F or C: ")

temp=int(temp)

    print ((temp-32)/1.8),"C"

elif(sel=="C"):
    print ((temp*1.8)+32),"F"

else:
    print "Input Error"
