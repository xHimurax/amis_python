print("Enter first number")
x=float(input())
print("Enter first number")
y=float(input())
print("Enter first number")
z=float(input())
if (x==y) and (y==z):
    answer=3
elif ((x==y) and (x!=z)) or ((y==z) and (x!=z)) or ((x==z) and (x!=y)):
    answer=2
else:
    answer=0
print(answer)
