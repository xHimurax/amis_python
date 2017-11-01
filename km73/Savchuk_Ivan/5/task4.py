kegleshar = [int(i) for i in input().split()]
a, b, c = [], [], []
k = 0
for i in range(kegleshar[0]):
    i += 1
    a.append(i)
    b.append(i)
print('a=',a)
for j in range(kegleshar[1]):
    d = [int(i) for i in input().split()]
    for i in range(d[0], d[1]+1):
        try:
            a.remove(i)
        except ValueError:
            k += 1
print('a1=', a)
for i in b:
        if i in a:
            i = 'I'
        else:
            i = '.'
        c.append(i)
print(''.join([str(i) for i in c]))