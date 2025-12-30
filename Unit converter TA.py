while True:

    print("Welcome to the Unit Converter 2000")
    print("1: km to mi")
    print("2: c to f")
    print("3: l to gal(US)")
    print("4: oz to lb")
    print("5: exit")
    choice=input("please enter your choice: ")
    if choice=="5":
        print("See you later!💩")
        break

    if choice=="1":
        a=(float(input("enter a dictance: ")))
        b=input("what is the unit: ")
        if b=="km":
            print(a*0.621371)
        if b=="mi":
            print(a/0.621371)

    if choice=="2":
        a1=(float(input("please enter a temperature: ")))
        b1=input("what is the unit: ")
        if b=="c":
            print(a1*9/5+32)
        if b=="f":
            print((a1-32)*5/9)
    if choice=="3":
        a2=(float(input("please enter a volume: ")))
        b2=input("what is the unit: ")
        if b2=="l":
            print(a2*3.785)
        if b2=="gal":
            print(a2/3.785)
    if choice=="4":
        a3=(float(input("please enter a weight: ")))
        b3=input("what is the unit: ")
        if b3=="oz":
            print(a3/16)
        if b3=="lb":
            print(a3*16)

    input("\nPress Enter to continue...")
