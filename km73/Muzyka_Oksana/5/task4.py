n, k = [int(s) for s in input("Enter n and k: " ).split()]
a = ['I'] * n
for i in range(k):
    l, r = [int(s) for s in input().split()]
    for j in range(l - 1, r):
        a[j] = '.'
print(''.join(a))
