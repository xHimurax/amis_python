x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))
a = (x1 + y1)
b = (x2 + y2)
if a - 2 <= b <= a + 2:
    print("YES")
elif b - 2 <= a <= b + 2:
    print("YES")
else:
    print("NO")