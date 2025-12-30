import random
a=random.randint(1,10)
while True :
    b=input("GUESS THE NUMBER: ")
    b=int(b)
    if b==a:
        print("CORRECT:)")
        break
    else :
        print("WRONG:(")