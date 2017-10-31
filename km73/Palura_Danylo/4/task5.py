print('      Task 5 \n')
a = int(input('Enter first number '))
b = int(input('Enter second number '))
c = int(input('Enter third number '))

if a == b == c:
    X = '1-st = 2-nd = 3-rd = '+str(a)
elif a == b != c:
    X = '1-st = 2-nd = '+str(a)
elif a == c != b:
    X = '1-st = 3-rd = '+str(a)
elif a != b == c:
    X = '2-nd = 3-rd = '+str(b)
else:
    X = 'No equal numbers'
#######################################################
print(X)
d=input('Press Enter to close')