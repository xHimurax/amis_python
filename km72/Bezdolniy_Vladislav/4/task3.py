import time
while True:
    x = input("Введите первое число:")
    y = input("Введите второе число:")
    z = input("Введите третье число:")
    if x < y < z:
        print(x, "является меньшим числом ")
    if x < z < y:
        print(x, "является меньшим числом ")
    if y < x < z:
        print(y, "является меньшим числом ")
    if y < z < x:
        print(y, "является меньшим числом ")
    if z < x < y:
        print(z, "является меньшим числом ")
    if z < y < x:
        print(z, "является меньшим числом ")
    if x == y == z:
        print("числа равны")
    while True:
        answer = input('Повоторить программу или выйти(да или нет)?: ')
        if answer in ('да', 'нет'):
            break
        print('Введите да или нет')
    if answer == 'да':
        continue
    else:
        print('Спасибо за использование.')
        time.sleep(2)
        exit()
