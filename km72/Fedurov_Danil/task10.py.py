x1 = int(input("Enter x1:"))
x2 = int(input("Enter x2:"))
y1 = int(input("Enter y1:"))
y2 = int(input("Enter y2:"))

if x1==y1 or x2==y2:
    print("YES")
elif (x1/y1)==(x2/y2):
    print("YES")
elif  (x1+x2)==(y1+y2)  or (x1-x2)==(y1-y2):
    print("YES")   
else:
    print("NO")
