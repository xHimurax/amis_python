a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a<=b and a<=c:
    answer=a
elif b<a and b<c:
    answer=b
else:
    answer=c
print("Smaller number is", answer)
input()
