x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

a = (x1 + y1)
b = (x2 + y2)
if a-2 <= b <= a+2:
    print("YES")
elif b-2 <= a <= b+2:
    print("YES")
else:
    print("NO")
