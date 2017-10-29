import math
x=int(input("Введіть число x: "))
y=int(input("Введіть число y: "))
x1=int(input("Введіть число x1: "))
y1=int(input("Введіть число y2: "))
if math.fabs(x-x1)==2 and math.fabs(y-y1)==1 or math.fabs(x-x1)==1 and math.fabs(y-y1)==2:
    print("Yes")
else:
    print("No")
