a = [int(i) for i in input().split()]
counter = 0
for i in a:
    for j in a:
        if i == j:
            counter += 1
counter -= 1
print(counter // 2)