n = int(input("n: "))
m = int(input("m: "))
k = int(input("k: "))

if n * m < k:
    result = "NO"
if not(k % m) or not(k % n):
    print("YES")
else:
    print("NO")
input()