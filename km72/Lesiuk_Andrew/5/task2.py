print('Програма скільки пар елементів, рівних один одному знаходиться у списку')
a = [int(a) for a in input('Введіть список\n').split()]
count = 0
for i in a:
    for b in a:
        if i == b:
            count = count+1
    count = count-1
print('Пар у списку:',count//2)
