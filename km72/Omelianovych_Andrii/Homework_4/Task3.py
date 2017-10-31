a = int(input('First: '))
b = int(input('Second: '))
c = int(input('Third: '))

if (a <= b) & (a <= c):
    number = a
elif (b <= a) & (b <= c):
    number = b
elif (c <= a) & (c <= b):
    number = c

print(number)