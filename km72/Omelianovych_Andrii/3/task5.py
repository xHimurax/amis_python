while 1:
    while 1:
        try:
            N = int(input('Number?: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    print('The next number for the number {0} is {2}.\nThe previous number for the number {0} is {1}.'.format(N, N-1, N+1))
    choice = str(
        input('Если вы желаете продолжить введите \"Да\". Для завершения программы введите любой символ.\nВвод: '))
    if choice.lower() == 'да':
        pass
    else:
        break