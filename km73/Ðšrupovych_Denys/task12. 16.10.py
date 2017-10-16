n = int(input())    #length of the bar
m = int(input())    #width of the bar
k = int(input())    #quantity of bars 
if n*m-k==a or n*m-k==b and n*m>k and k!=1:
    print('YES')
elif (n*m-k)%2==0 and n*m>k and k!=1:
    print('YES')
else:
    print('NO')
input()
