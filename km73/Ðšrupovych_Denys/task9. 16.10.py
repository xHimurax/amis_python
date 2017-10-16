x1 = int(input())   #Enter integer number of column where bishop is located
x2 = int(input())   #Enter integer number of row where bishop is located
y1 = int(input())   #Enter integer number of column where bishop must be moved
y2 = int(input())   #Enter integer number of row where bishop must be moved
if (x1/y1)==(x2/y2):
    print('YES')
elif (x1+x2)==(y1+y2):
    print('YES')
else:
    print('NO')
input()
