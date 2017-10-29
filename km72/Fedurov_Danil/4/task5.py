x = int(input("Enter x:"))
y = int(input("Enter y:"))
z = int(input("Enter z:"))
if x == y == z:
    print(3)
elif y==x and x!=z:
    print(2)
elif y!=x and x==z:
    print(2)
elif x!=y and y==z:
    print(2)
elif x!=y!=z:
    print(0)
