n = int(input('Введіть кількість кегель: '))
k = int(input('Введіть кількість куль: '))
a = []
for i in range(1, n+1 ):
    a.append(str('I'))
for p in range(k):
  b = []
  for i in range(0,1):
    b.append(int(input('Введіть першу збиту кеглю: ')))
    b.append(int(input('Введіть останню збиту кеглю: ')))
    for j in range(b[0]-1,b[1]):
        a[j]=str('.')

print(''.join( str(n) for n in a))