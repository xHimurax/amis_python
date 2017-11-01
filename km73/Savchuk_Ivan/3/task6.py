x = int(input('please enter init coordinate x:',))
y = int(input('please enter init coordinate y:',))
x1 = int(input('please enter coordinate x1:',))
y1 = int(input('please enter coordinate y1:',))
if (x == x1) & (1 <= y <= 8) & (1 <= y1 <= 8):
    print('YES')
elif (y == y1) & (1 <= x <= 8) & (1 <= x1 <= 8):
    print('YES')
else:
    if (x != x1) | (y != y1):
        print('NO')