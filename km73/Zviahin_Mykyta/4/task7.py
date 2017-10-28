x1 = int(input("Enter first coordinate for first place: "))
y1 = int(input("Enter second coordinate for first place: "))
x2 = int(input("Enter first coordinate for second place: "))
y2 = int(input("Enter second coordinate for second place: "))

if (((x1 + y1)//2 == 0) & ((x2 + y2)/2 == 0)) or (((x1 + y1)//2 == 1) & ((x2 + y2)//2 == 1)):
    print("Yes")
else:
    print("No")

input()

    
