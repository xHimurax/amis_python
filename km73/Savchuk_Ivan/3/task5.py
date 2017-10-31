a = int(input('enter firs number:',))
b = int(input('enter second number:',))
c = int(input('enter third number:',))
if a == b == c:
    print('3')
elif a == b != c or a == c != b or b == c != a:
    print('2')
else:
    if a != b != c:
        print('0')

