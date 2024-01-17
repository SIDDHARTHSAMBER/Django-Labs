#WIFI

print("Reboot the Computer and try to connect")
print("Did that fix the problem")

res1=input("Yes or No\n")
if res1=="Yes":
    print("Congrats")
elif res1=="No":
    print("Reboot the router and try to connect")
    print("Did that fix the problem")
    res2=input("Yes or No\n")
    if res2=="Yes":
        print("Congrats")
    elif res2=="No":
        print("Make Sure the cables between the router and modem are plugged in firmly")
        print("Did that fix the problem")
        res3=input("Yes or No\n")
        if res3=="Yes":
            print("Congrats")
        elif res3=="No":
            print("Move the router to a new location and try to connect")
            print("Did that fix the problem")
            res4=input("Yes or No\n")
            if res4=="Yes":
                print("Congrats")
            elif res4=="No":
                print("Get a New Router")
            else:
                print("Enter Valid Input")
        else:
            print("Enter Valid Input")            
    else:
        print("Enter Valid Input")
else:
    print("Enter Valid Input")
