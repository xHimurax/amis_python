n=int(input("Enter N: "))
m=int(input("Enter M: "))
k=int(input("Enter K: "))
if n*m-k==n or n*m-k==m and n*m>k and k!=1:
   print('YES')
elif (n*m-k)%2==0 and n*m>k and k!=1:
   print('YES')
else:
   print('NO')
