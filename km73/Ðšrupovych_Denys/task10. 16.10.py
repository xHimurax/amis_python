x1 = int(input())   #Enter integer number of column where queen is located
x2 = int(input())   #Enter integer number of row where queen is located
y1 = int(input())   #Enter integer number of column where queen must be moved
y2 = int(input())   #Enter integer number of row where queen must be moved
if x1==y1 or x2==y2:
       print('YES')
elif (x1/y1)==(x2/y2):
    print('YES')
elif (x1+x2)==(y1+y2) or (x1-x2)==(y1- y2):
    print('YES')
else:
    print('NO')
input()
