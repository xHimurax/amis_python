x1 = int(input("Enter the first coodinate of the initial place: "))
y1 = int(input("Enter the second coordinate of the initial place: "))
x2 = int(input("Enter the first coordinate for final place: "))
y2 = int(input("Enter the second coordinate for final place: "))

if ((x1 == x2) or (x1 == x2 +1) or (x1 == x2 -1)) & ((y1 == y2) or (y1 == y2 +1) or (y1 == y2 -1)):
    print("Yes")
else:
    print("No")

input()
    
