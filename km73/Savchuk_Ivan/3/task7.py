x = int(input('please enter init coordinate x:',))
y = int(input('please enter init coordinate y:',))
x1 = int(input('please enter coordinate x1:',))
y1 = int(input('please enter coordinate y1:',))
if (x+x1+y+y1) % 2 == 0:
    print('YES')
elif (x+x1+y+y1) % 2 !=0:
    print('Yes')
else:
    print('NO')