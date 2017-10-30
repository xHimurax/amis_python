a = input ('Enter the height of each: ').split()
b = input('Enter the height of Peter: ' )
n = 1
for i in range(0,len(a)):
    a[i] = int(a[i])
    if int(b) <= a[i]:
        n += 1
print(n)
