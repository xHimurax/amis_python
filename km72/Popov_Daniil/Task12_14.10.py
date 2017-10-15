print('starting program')
n=int(input('enter length'))
m=int(input('enter width'))
k=int(input('enter squares'))
if (k%n==0 and k/n<=m) or (k%m==0 and k/m<=n):
    print('yes')
else:
    print('no')
