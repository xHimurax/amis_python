a = [int(a) for a in input().split()]
number = 0
height = int(input())
for i in range(0, len(a)):
    if a[i] >= height:
        number += 1
print(number + 1)