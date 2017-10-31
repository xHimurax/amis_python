x = int(input('please enter init coordinate x:',))
y = int(input('please enter init coordinate y:',))
x1 = int(input('please enter coordinate x1:',))
y1 = int(input('please enter coordinate y1:',))
d1 = abs(x-x1)
d2 = abs(y-y1)
if d1 == 1 and d2 == 0:
    print('YES')
elif d2 == 1 and d1 == 0:
    print('YES')
elif d1 == d2:
    print('NO')
else:
    print('NO')

