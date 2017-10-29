
n = int(input('Введіть число n: '))
m = int(input('Введіть число m: '))
k = int(input('Введіть число k: '))
a = n%2
b = m%2
if (a == 0 and k == (n/2)*m) or (b == 0 and k == (m/2)*n):
    answer = 'YES'
else:
    answer = 'NO'

print(answer)