a=float(input("Enter a number: "))
b=float(input("Enter another number: "))
c=input("Enter the symbol: ")
if c=="+":
    print(a+b)
if c=="-":
    print(a-b)
if c=="*":
    print(a*b)
if c=="/":
    if b==0:
        print("Division by zero")
    else:
        print(a/b)
