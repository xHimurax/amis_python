a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if (a <= b) & (a <= c):
    number = a
elif (b <= a) & (b <= c):
    number = b
elif (c <= a) & (c <= b):
    number = c

print(number)