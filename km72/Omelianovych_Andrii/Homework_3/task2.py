while 1:
    while 1:
        try:
            a = float(input('Первый катет: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    while 1:
        try:
            b = float(input('Второй катет: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    print('S =',0.5*a*b)
    choice = str(
        input('Если вы желаете продолжить введите \"Да\". Для завершения программы введите любой символ.\nВвод: '))
    if choice.lower() == 'да':
        pass
    else:
        break