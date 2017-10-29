a = input("Введіть список : \n").split()
k = int(input())
print(" ".join([" ".join(a[:k:]) + " " + " ".join(a[k+1::])]))
