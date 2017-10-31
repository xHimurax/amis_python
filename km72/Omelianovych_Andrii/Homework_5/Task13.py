a = [int(a) for a in input().split()]
count = 0
for i in a:
    for b in a:
        if i == b:
            count += 1
    count -= 1
print(count//2)