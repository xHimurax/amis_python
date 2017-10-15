a = int(input("Enter first  number: "))
b = int(input("Enter second  number: "))
c = int(input("Enter third  number: "))

if (c < a) & (c < b):
    print("The smallest number is ",c)
elif (a < b) & (a < c):
    print("The smallest number is ",a)
else:
    print("The smallest number is ",b)

