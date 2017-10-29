s = input("Введіть послідовність чилел\n")
a = s.split()
n=len(a)
b=0
for i in range(n):
    a[i]=int(a[i])

for i in range(n):
    if i==n-1:
        break
    elif a[i]==a[i+1]:
        b=b+1
print(b)
