a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a==b==c:
    answer=3
elif (a==b and b!=c) or (b==c and a!=b) or (a==c and a!=b):
    answer=2
else:
    answer=0
print(answer)
input()
