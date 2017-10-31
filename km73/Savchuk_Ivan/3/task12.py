n = int(input("enter the lenght:",))
m = int(input("enter the heigh:",))
k = int(input("enter the number of needed cells:",))
if (n*m-k) % 2 == 0 and k != 1 and n*m > 2:
    print('YES')
elif n*m-k==n or n*m-k==m and n*m>k and k!=1:
    print('YES')
else:
    print('NO')