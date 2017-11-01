x = int(input('please enter init coordinate x:',))
y = int(input('please enter init coordinate y:',))
x1 = int(input('please enter coordinate x1:',))
y1 = int(input('please enter coordinate y1:',))
d1 = abs(x/y)
d2 = abs(x1/y1)
d3 = abs(y+y1)
d4 = abs(x+x1)
if (x == x1) & (1 <= y <= 8) & (1 <= y1 <= 8):
    print('YES')
elif (y == y1) & (1 <= x <= 8) & (1 <= x1 <= 8):
    print('YES')
if d3 == d4 :
    print('YES')
elif d1 != d2 :
        print('NO')
else:
    print('NO')