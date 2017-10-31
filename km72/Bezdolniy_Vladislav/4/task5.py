import time
while True:
    year = float(input("Введите год :"))
    if (not year % 4 and year % 100) or not year % 400:
        print('LEAP')
    else:
        print('COMMON')
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
