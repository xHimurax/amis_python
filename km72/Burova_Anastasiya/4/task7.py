x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))
a = (x1 + y1)
b = (x2 + y2)
if (a % 2 == 0) and (b % 2 == 0):
    print("YES")
elif(a % 2 != 0) and (b % 2 != 0):
    print("YES")
else:
    print("NO")