x1 = int(input('X1: '))
y1 = int(input('Y1: '))
x2 = int(input('X2: '))
y2 = int(input('Y2: '))
if (x1 < 1 or x2 > 8) or (x2 < 1 & x2 > 8) or (y1 < 1 & y1 > 8) or (y2 < 1 & y2 > 8):
    print('GOODBYE!')
    exit()
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")