x = int(input('please enter init coordinate x:',))
y = int(input('please enter init coordinate y:',))
x1 = int(input('please enter coordinate x1:',))
y1 = int(input('please enter coordinate y1:',))
d1 = abs(x/y)
d2 = abs(x1/y1)
d3 = abs(y+y1)
d4 = abs(x+x1)
if d1 == d2 | d3 == d4:
    print('YES')
elif d1 != d2 | d3 != d4:
    print('NO')
else:
    print('NO')