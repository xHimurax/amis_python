import time
while True:
    x = input("Введите первое число:")
    y = input("Введите второе число:")
    if x < y:
        print(x, "является меньшим числом ")
    if x > y:
        print(y, "является меньшим числом ")
    if x == y:
        print("Первое число равняется второму.")
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