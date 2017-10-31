a = input().split()
x = int(input())
v = 0
for i in range(0, len(a)):
    n = int(a[i])
    if n >= x:
        v = i + 1
print('boys number:', v + 1)