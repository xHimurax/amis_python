a = input().split()
k = int(input())
print(" ".join([" ".join(a[:k:]) + " " + " ".join(a[k+1::])]))