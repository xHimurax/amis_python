x1 = int(input("Enter first coordinate for initial place: "))
y1 = int(input("Enter second coordinate for initial place: "))
x2 = int(input("Enter first coordinate for final place: "))
y2 = int(input("Enter second coordinate for final place: "))

import math

delx = abs(x1 - x2)
dely = abs(y1 - y2)

if ((delx == 2) & (dely == 1)) or ((delx == 1) & (dely == 2)):
    answer = "Yes"
else:
    answer = "No"
    
print(answer)

input()

    
