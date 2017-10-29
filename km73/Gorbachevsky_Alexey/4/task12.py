n=int(input("Enter n: "))
m=int(input("Enter m: "))
k=int(input("Enter k: "))

if ((k%n == 0) & (k//n < m)) | ((k%m == 0) & (k/m < n)):
    result = "YES"
else:
    result = "NO"

print(result)
