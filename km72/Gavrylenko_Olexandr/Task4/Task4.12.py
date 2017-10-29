n = int(input('Enter chocolate length(n):'))
m = int(input('Enter chocolate width(m):'))
k = int(input('Enter number of squares you want to get(k):'))
if k>n*m or k%m != 0 and k%n != 0:
    print('NO')
else:
    print('YES')
