x = int(input('please enter init coordinate x:',))
y = int(input('please enter init coordinate y:',))
x1 = int(input('please enter coordinate x1:',))
y1 = int(input('please enter coordinate y1:',))
if abs(x1-x) == 1 and abs(y1-y) == 2:
    print('YES')
else:
    print('NO')
