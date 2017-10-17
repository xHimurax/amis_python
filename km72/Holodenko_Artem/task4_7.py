x=int(input("Введіть число x: "))
y=int(input("Введіть число y: "))
x1=int(input("Введіть число x1: "))
y1=int(input("Введіть число y2: "))
if x%2==x1%2 and y%2==y1%2:
    print("Yes")
elif x%2==y1%2 and y%2==x1%2:
    print("Yes")
else:
    print("No")
