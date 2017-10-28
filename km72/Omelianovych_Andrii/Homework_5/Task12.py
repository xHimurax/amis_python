a = input().split()
index = input().split()
k = int(index[0])
c = index[1]

a = " ".join(a[:k:]) + " " + c + " " + " ".join(a[k::])
print(a)