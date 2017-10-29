x1 = int(input("Enter first coordinate for initial place: "))
y1 = int(input("Enter second coordinate for initial place: "))
x2 = int(input("Enter first coordinate for final place: "))
y2 = int(input("Enter second coordinate for final place: "))

import math

delx = abs(x1-x2)
dely = abs(y1-y2)

if (delx == dely) or (x1 + y1) == (x2 + y2):
    print("Yes")
else:
    print("No")

input()

