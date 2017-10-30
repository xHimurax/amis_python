print('      Task 12 \n')
m = int(input('Enter number of chocolate cells in horizontal row '))
n = int(input('Enter number of chocolate cells in vertical row '))
k = int(input('Enter number of chocolate cells you want to get '))
if (m>0)&(n>0)&(0<k)&(k<=m*n):
    if (k%m==0) | (k%n==0):
        X = 'Yes'
    else:
        X = 'No'
else:
    X='Uncorrect data'
#######################################################
print(X)
d=input('Press Enter to close')