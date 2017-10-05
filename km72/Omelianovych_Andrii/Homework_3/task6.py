while 1:
    while 1:
        try:
            A = int(input('First group: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    while 1:
        try:
            B = int(input('Second group: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    while 1:
        try:
            C = int(input('Third group: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    f = (A + B + C)%2
    if f == 0:
        print('Count of desks: {}'.format(int((A + B + C)/2)))
    else:
        print('Count of desks: {}'.format(int((A + B + C)/2+1)))
    choice = str(
        input('Если вы желаете продолжить введите \"Да\". Для завершения программы введите любой символ.\nВвод: '))
    if choice.lower() == 'да':
        pass
    else:
        break