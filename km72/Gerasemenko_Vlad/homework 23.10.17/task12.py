a = input("Введіть список 1: \n").split()
index = input("Введіть список 2: \n").split()
k = int(index[0])
c = index[1]
a = " ".join(a[:k:])+" "+c+" "+" ".join(a[k::])
print(a)
