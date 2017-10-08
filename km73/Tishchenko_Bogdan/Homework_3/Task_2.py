print("Enter first cathetus length: ")
a = float(input())
print("Enter second cathetus length: ")
b = float(input())

S = a*b/2

if a<0 or b<0:
    print("Improper values")
else:
    
    print("The area of the right triangle is ", S)
