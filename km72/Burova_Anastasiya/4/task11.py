x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))
if (abs(x1 - x2) == 2) and (abs(y1 - y2) == 1):
    print("YES")
elif (abs(x1 - x2) == 1) and (abs(y1 - y2) == 2):
    print("YES")
else:
    print("NO")

