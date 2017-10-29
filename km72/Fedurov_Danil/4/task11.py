x1 = int(input("Enter x1 :"))
x2 = int(input("Enter x2 :"))
y1 = int(input("Enter y1 :"))
y2 = int(input("Enter y2 :"))
if abs(x1-y1)==2 and abs(x2-y2)==1:
    print("YES")
elif abs(x1-y1)==1 and abs(x2-y2)==2:
    print("YES")
else:
    print("NO")
