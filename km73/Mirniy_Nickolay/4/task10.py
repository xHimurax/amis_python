x1 = int(input('x1 : '))
y1 = int(input('y1 : '))
x2 = int(input('x2 : '))
y2 = int(input('y2 : '))

if (0 < x1 < 9 ) & (0 < y1 < 9) & (0 < x2 < 9) & (0 < y2 < 9) :
    if (abs(x1-x2)) == (abs(y2 - y1)) or (x1 == x2) or (y1 == y2 ) :
        answer = 'YES'
    else :
        answer = 'NO'
else :
    answer = 'NO'
print(answer)