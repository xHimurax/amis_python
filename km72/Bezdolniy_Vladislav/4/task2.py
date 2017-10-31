import time
while True:
    x = float(input("Введите число x = "))
    if x > 0:
        print("sgn(x) = 1")
    if x < 0:
        print("sgn(x) = -1")
    if x == 0:
        print("sgn(x) = 0")
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