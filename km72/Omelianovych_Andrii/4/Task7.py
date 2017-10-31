x1 = int(input('X1: '))
y1 = int(input('Y1: '))
x2 = int(input('X2: '))
y2 = int(input('Y2: '))
if (x1 < 1 or x2 > 8) or (x2 < 1 & x2 > 8) or (y1 < 1 & y1 > 8) or (y2 < 1 & y2 > 8):
    print('GOODBYE!')
    exit()
if (x1+y1)//2 == 0:
    color1 = 'BLACK'
else:
    color1 = 'NOT BLACK'

if (x2+y2)//2 == 0:
    color2 = 'BLACK'
else:
    color2 = 'NOT BLACK'

if color1 == color2:
    print('YES')
else:
    print('NO')