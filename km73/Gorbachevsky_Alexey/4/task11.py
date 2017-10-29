x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if ((dx == 1)&(dy == 2)) | ((dx == 2 )&(dy == 1)):
    result = "YES"
else:
    result = "NO"

print(result)
