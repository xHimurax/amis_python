x=int(input("Enter x: "))
y=int(input("Enter y: "))
z=int(input("Enter z: "))
if (z<x) and (z<y):
    print("Z is lower: ", z)
elif (x<z) and (x<y):
    print("X is lower: ", x)
elif (y<z) and (y<x):
    print("Y is lower: ", y)
elif x==y and x<z:
    print("X and Y are simple and lower then Z. X = Y = ", x)
elif x==z and x<y:
    print("X and Z are simple and lower then Y. X = Z = ", x)
else:
    print("All digit are simple")
