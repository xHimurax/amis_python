a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a==b==c:
    print("3")
elif a==b and b!=c:
    print("2")
elif a==c and b!=c:
    print("2")
elif c==b and a!=c:
    print("2")
elif c!=b and a!=c and a!=b:
    print("0")
input("")
