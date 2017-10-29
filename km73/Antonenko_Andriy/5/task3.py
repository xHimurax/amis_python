a = [int(s) for s in input('Введіть елементи списку : ').split( )]
b = []
for j in range(0, len(a)):
    one = a.count(a[j])
    if one == 1:
        b.append(a[j])
answer = b

print('Список унікальних елементів: '+str(answer) )
