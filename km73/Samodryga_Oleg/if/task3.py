a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if c<a and c<b:
    print("min-third")
elif a<c and a<b:
    print("min-first")
elif b<a and b<c:
    print("min-second")
input("")
