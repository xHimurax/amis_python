import math
x=int(input("Введіть число x: "))
y=int(input("Введіть число y: "))
x1=int(input("Введіть число x1: "))
y1=int(input("Введіть число y2: "))
if x==x1 and y==y1:
    print("No")
elif  math.fabs(x-x1)==0 or math.fabs(x-x1)==1 and math.fabs(y-y1)==0 or math.fabs(y-y1)==1:
    print("Yes")
else:
    print("No")
