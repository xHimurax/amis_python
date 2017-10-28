a = input().split()
count = 0
for i in range(1, len(a)):
    if a[i-1] != a[i]:
        count += 1
print(count+1)