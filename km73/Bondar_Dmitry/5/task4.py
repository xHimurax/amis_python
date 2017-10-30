n = int(input("Введіть кількість кеглів: "))
k = int(input("Введіть кількість кидків: "))
ans = []
K=0
for i in range(1 , k+1):
    K+=i
if (n - 2*K) >= 1:
	if (n-2*k)%2==1:
		li=(n-2*K)//2+1
		lr=(n-2*K)//2
	else:
		li=(n-2*K)//2+1
		lr=(n-2*K)//2-1
	for i in range(1 , li):
		ans.append(i)
	for i in range(2*K):
		ans.append(".")
	for i in range(n-lr , n+1):
		ans.append(i)
else:
    for i in range(n):
        ans.append(".")
print(ans)
