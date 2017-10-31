while 1:
    while 1:
        try:
            a = str(input('Ваше имя: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    print('Hello, {0}!'.format(a))
    choice = str(
        input('Если вы желаете продолжить введите \"Да\". Для завершения программы введите любой символ.\nВвод: '))
    if choice.lower() == 'да':
        pass
    else:
        break