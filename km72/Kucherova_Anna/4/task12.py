n = int(input("Введіть ширину: "))
m = int(input("Введіть довжину: "))
k = int(input("Клітин у частині: "))

if n >= m:
    if (k >= m) & (k % m == 0):
        print("YES")
    else:
        print("NO")
    
if m >= n:
    if (k >= n) & (k % n == 0):
        print("YES")
    else:
        print("NO")

