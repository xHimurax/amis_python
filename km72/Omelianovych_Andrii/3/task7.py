while 1:
    while 1:
        try:
            N = int(input('Minutes?: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    minutes = N % 60
    hours = N % 1440
    hours2 = hours // 60
    print('Time: {0:02d}:{1:02d}'.format(hours2, minutes))
    choice = str(
        input('Если вы желаете продолжить введите \"Да\". Для завершения программы введите любой символ.\nВвод: '))
    if choice.lower() == 'да':
        pass
    else:
        break