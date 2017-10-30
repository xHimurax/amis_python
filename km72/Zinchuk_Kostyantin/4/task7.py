a1=int(input("Enter row 1: "))
b1=int(input("Enter col 1: "))
a2=int(input("Enter row 2: "))
b2=int(input("Enter col 2: "))
if (a1 or a2 or b1 or b2)<1 or (a1 or a2 or b1 or b2)>8:
    print("Error")
elif (a1+b1)%2!=0 and (a2+b2)%2!=0:
    print("YES")
elif (a1+b1)%2==0 and (a2+b2)%2==0:
    print("YES")
else:
    print("NO")
