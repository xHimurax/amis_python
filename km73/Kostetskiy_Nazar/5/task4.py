N,K = [int(i) for i in input().split()]
left = [0]*K
right = [0]*K
keglya = ['I']*N
for i in range(0, K):
    left[i],right[i] = [o for o in input().split()]
    for j in range(int(left[i]),int(right[i])+1):
        keglya[j] = '.'
print("".join(keglya))
