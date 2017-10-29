a = [int(i) for i in input().split()]

a = [i for i in a if a.count(i)==1]
result = " ".join([str(i) for i in a])

print(result)
