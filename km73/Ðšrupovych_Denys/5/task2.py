num = [int(s) for s in input().split()]
pairs = 0
for i in range(len(num)):
     for j in range(i + 1, len(num)):
               if num[i] == num[j]:
                   pairs += 1
print(pairs)
input()
