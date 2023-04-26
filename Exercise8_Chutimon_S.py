userinput = input("Username:")
paswordinput = input("Password:")

if (userinput == "admin" and paswordinput == "567"):
    print ("------Welcome to RobbyShop------")
    print ("1.Orange = 10 บาท/ผล")
    print ("2.Apple = 20 บาท/ผล")
    print ("3.Banana = 9 บาท/ผล")
    userselected = int(input("What do you want?>>"))
    
    if userselected==1:
        o = int(input("How many?:"))
        print("Price total =",o*10,"บาท")
    elif userselected==2:
        a = int(input("How many?:"))
        print("Price total =",a*20,"บาท")
    elif userselected==3:
        b = int(input("How many?:"))
        print("Price total =",b*9,"บาท")
    print("Thank you to buy :)")
else:
    print("---Username or Password Error---")
    print("---Please Sigin again---")
    

    
       
    
    