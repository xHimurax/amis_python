print("Enter first number")
x=float(input())
print("Enter second number")
y=float(input())
print("Enter third number")
z=float(input())
if (x<y) and (x<z):
    answer=x
elif (y<x) and (y<z):
    answer=y
elif (z<x) and (z<y):
    answer=z
print(answer)
