while 1:
    while 1:
        try:
            N = int(input('Скільки студентів?: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    while 1:
        try:
            K = int(input('Скільки яблук?: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    count = K // N
    apples = K % N
    print('У кожного {0} студента яблук, у кошику залишилось {1} яблук.'.format(count, apples))
    choice = str(
        input('Если вы желаете продолжить введите \"Да\". Для завершения программы введите любой символ.\nВвод: '))
    if choice.lower() == 'да':
        pass
    else:
        break