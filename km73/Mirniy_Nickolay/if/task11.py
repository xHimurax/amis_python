x1 = int(input('x1 : '))
y1 = int(input('y1 : '))
x2 = int(input('x2 : '))
y2 = int(input('y2 : '))

if (0 < x1 < 9 ) & (0 < y1 < 9) & (0 < x2 < 9) & (0 < y2 < 9) :
    if (x2==x1+2 )or (x2==x1-2) & (y2 == y1+1)or(y2 == y1-1):
        answer = 'YES'
    elif (x2==x1+1)or(x2==x1-1) & (y2==y1+2)or(y2==y1-2):
        answer = 'YES'
    else :
        answer = 'NO'
else :
    answer = 'NO'
print(answer)