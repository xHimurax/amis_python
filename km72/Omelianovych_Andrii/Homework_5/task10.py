a = [int(a) for a in input().split()]
index_max = 0
index_min = 0
for i in range(0, len(a)):
    if a[i] > a[index_max]:
        index_max = i
    if a[i] < a[index_min]:
        index_min = i
a[index_max], a[index_min] = a[index_min], a[index_max]
print(' '.join([str(i) for i in a]))
