a = [int(a) for a in input().split()]
count = 0
for i in a:
    for j in a:
        if i == j:
            count += 1
    count -= 1
    if count == 0:
        print(i, end=' ')
    count = 0
