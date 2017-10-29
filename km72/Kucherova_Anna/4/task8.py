x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

a = (x1 + y1)
b = (x2 + y2)
if (abs(x1-x2)==1 or abs(x1-x2)==0) and (abs(y1-y2)==1 or abs(y1-y2)==0):
    print("YES")
    
else:
    print("NO")
