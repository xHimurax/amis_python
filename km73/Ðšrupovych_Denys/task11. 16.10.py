x1 = int(input())   #Enter integer number of column where knight is located
x2 = int(input())   #Enter integer number of row where knight is located
y1 = int(input())   #Enter integer number of column where knight must be moved
y2 = int(input())   #Enter integer number of row where knight must be moved
if abs(x1-y1)==2 and abs(x2-y2)==1:
    print('YES')
elif abs(x1-y1)==1 and abs(x2-y2)==2:
    print('YES')
else:
    print('NO')
input()
