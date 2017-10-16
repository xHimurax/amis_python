x1 = int(input())   #Enter integer number of column where king is located
x2 = int(input())   #Enter integer number of row where king is located
y1 = int(input())   #Enter integer number of column where king must be moved
y2 = int(input())   #Enter integer number of row where king must be moved
if -1<=(x1- y1)<=1 and -1<=(x2- y2)<=1:
   print('YES')
else:
   print('NO')
input()
