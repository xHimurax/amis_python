a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a == b == c:
    num = 3
elif a == b or a==c or b==c:
    num = 2
else:
    num = 0
print(num)