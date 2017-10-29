x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))

if (x1 + y1)%2 == (x2 + y2)%2:
    result = "YES"
else:
    result = "NO"

print(result)
