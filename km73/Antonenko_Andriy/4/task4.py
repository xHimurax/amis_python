
year = int(input('Введіть рік : '))
k = year%4
l = year%100
f = year%400
if (k == 0 & l == 0) or f == 0:
    answer = 'LEAP'
else:
    answer = 'COMMON'

print(answer)