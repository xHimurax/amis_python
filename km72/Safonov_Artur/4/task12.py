
n = int(input("Введіть n: "))
m = int(input("Введіть m: "))
k = int(input("Введіть k: "))

if (k%m == 0 or k%n == 0) and k<=m*n:
    print("YES")
else:
    print("NO")
