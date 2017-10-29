a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
x=int(input("Enter number x: "))
y=int(input("Enter number y: "))
if a<1 or a>8 or b<1 or b>8 or x<1 or x>8 or y<1 or y>8:
    print("Try to enter the correct number")
elif x==a and y==b:
    print("NO")
elif (x==a or x==a+1 or x==a-1) and (y==b or y==b+1 or y==b-1):
    print("YES")
else:
    print("NO")
input()
