a = [int(a) for a in input().split()]
max = a[0]
for i in range(0, len(a)):
    if a[i] > max:
        max = a[i]
        max_i = i
print(max, max_i)