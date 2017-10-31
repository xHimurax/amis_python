while 1:
    while 1:
        try:
            a = float(input('A: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    while 1:
        try:
            b = float(input('B: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    while 1:
        try:
            c = float(input('C: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    print('A + B + C =',a+b+c)
    choice = str(
        input('Если вы желаете продолжить введите \"Да\". Для завершения программы введите любой символ.\nВвод: '))
    if choice.lower() == 'да':
        pass
    else:
        break