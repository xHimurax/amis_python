print('Програма виводить елементи списку які зустрічається тільки один раз')
a = [int(a) for a in input('Bведіть список').split()]
x = 0
for i in a:
    for b in a:
        if i == b:
            x = x+1
    x= x-1
    if x == 0:
        print(i, end=' ')
    x = 0
