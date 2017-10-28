a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a < b) & (a < c):
    print("Number ", a, " is the smaller")
elif (b < a) & (b < c):
    print("Number ", b, " is the smaller")
elif (c < a) & (c < b):
    print("Number ", c, " is the smaller")
elif (a == b) &(b == c):
    print("All numbers are equal")
elif (a < b) & (a == c):
    print("First and third numbers are the smaller")
elif (b < c) & (b == a):
    print("First and second numbers are the smaller")
elif (b < a) & (c == b):
    print("Second and third numbers are the smaller")

input()
