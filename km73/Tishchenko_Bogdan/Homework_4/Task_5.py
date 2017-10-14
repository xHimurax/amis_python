a = int(input("Enter the first number\n"))
b = int(input("Enter the first number\n"))
c = int(input("Enter the first number\n"))

if a==b==c:
    answer = 3
elif a==b or a==c or b==c:
    answer = 2
else:
    answer = 0
print(answer)
