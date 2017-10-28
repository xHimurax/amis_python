n  = int(input('Number of rows : '))
m  = int(input('Number of columns : '))
k  = int(input('Number of cells after separate : '))

if (n>0)&(m>0)&(k>0) :
    if (k < m*n) & (k%n==0) or (k%m==0) :
        answer = 'YES'
    else :
        answer = 'NO'
else :
    answer = 'Error'
print(answer)

