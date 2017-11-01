a = input().split() # например 1 1 1 1 1
print(sum(a.count(x) - 1 for x in a) // 2)