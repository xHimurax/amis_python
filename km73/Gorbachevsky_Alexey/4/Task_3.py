a=int(input("Enter first_number: "))
b=int(input("Enter second_number: "))
c=int(input("Enter third_number: "))

result = "Minimum of 3 numbers is: "

if (a>b)&(a>c):
    a,b,c=b,c,a

if (a>b):
    a,b,c=b,a,c

result += str(a)

print(result)
