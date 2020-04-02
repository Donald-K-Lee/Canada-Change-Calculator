#Title: Canada Change Calculator
#By: Donald Lee

#Forms of change, and their starting value
hundred=0
fifty=0
twenty=0
ten=0
five=0
toonie=0
loonie=0
quarter=0
dime=0
nickel=0
#End

change = float(input("How much change will they recieve?:"))
def remain():
    global dime
    def conclude():
        global dime
        if change == 0.04 or change == 0.03:
            global nickel
            nickel = 2
            conclude()
            if nickel == 2:
                dime = dime + 1
                nickel = 0
                conclude()
            else:
                conclude()
        elif dime >= 1:
            print("You owe " + str(dime) + " dime(s)")
            dime=0
            conclude()
        elif nickel==1:
            print("You owe a nickel")
        else:
            print("Done")
    global change #makes change global, so that when change is decreased, it would remain decreased for the entire program
    change = round(change, 2) #ensures that change isn't irrational
    if change >=100:
        hundred = change //100 #Number of times 100 went into the change
        change = change % 100  # Remainder of the answer
        print("You owe " + str(hundred) +" 100 dollar bill(s)")
        remain()
    elif change >=50:
        fifty = change//50
        change= change % 50
        print("You owe a 50 dollar bill") #You can only owe 1 50 dollar bill, since 2 fifties would make 100
        remain()
    elif change >=20:
        twenty = change//20
        change= change % 20
        print("You owe " + str(twenty) + " 20 dollar bill(s)")
        remain()
    elif change >=10:
        ten = change//10
        change= change % 10
        print("You owe " + str(ten) + " 10 dollar bill(s)")
        remain()
    elif change >=5:
        five = change//5
        change= change % 5
        print("You owe " + str(five) + " 5 dollar bill(s)")
        remain()
    elif change >=2:
        toonie = change//2
        change= change % 2
        print("You owe " + str(toonie) + " toonie(s)")
        remain()
    elif change >=1:
        loonie = change//1
        change= change % 1
        print("You owe " + str(loonie) + " loonie(s)")
        remain()
    elif change >=0.25:
        quarter = change//0.25
        change= change % 0.25
        print("You owe " + str(quarter) + " quarter(s)")
        remain()
    elif change >=0.1:
        dime = change//0.1
        change= change % 0.1
        dime=dime
        remain()
    elif change >=0.05:
        global nickel
        nickel = change//0.05
        change= change % 0.05
        nickel=1
        remain()
    elif nickel==1:
        nickel = 1
        conclude()
    else:
        conclude()
remain()