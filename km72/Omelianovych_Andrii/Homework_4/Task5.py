a = int(input('First: '))
b = int(input('Second: '))
c = int(input('Third: '))

if a == b == c:
    number = 3
elif a == b or b==c or a==c:
    number = 2
else:
    number = 0
print(number)