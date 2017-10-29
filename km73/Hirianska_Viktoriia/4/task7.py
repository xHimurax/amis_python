a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
x=int(input("Enter number x: "))
y=int(input("Enter number y: "))
if a<1 or a>8 or b<1 or b>8 or x<1 or x>8 or y<1 or y>8:
    print("Try to enter the correct number")
elif x==a and y==b:
    print("NO")
elif (a+x)%2==0 and (b+y)%2==0:
    print("YES")
elif (a+x)%2!=0 and (b+y)%2!=0:
    print("YES")
else:
    print("NO")
input()
