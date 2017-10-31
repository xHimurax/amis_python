x1 = int(input())    #Enter integer number of column where rook is located
x2 = int(input())    #Enter integer number of row where rook is located
y1 = int(input())    #Enter integer number of column where rook must be moved
y2 = int(input())    #Enter integer number of row where rook must be moved
if x1==y1 or x2==y2:
    print('YES')
else:
    print('NO')
input()
