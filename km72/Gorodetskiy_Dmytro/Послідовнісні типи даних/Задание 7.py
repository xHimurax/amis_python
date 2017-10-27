test = []
while True:#цикл для ввода переменной
    try:
        N = int(input("Введите количество учеников:")) #ввод количества элементов в списке
        if N <= 0: #условие ввода отрицательных чисел
            print("Количество учеников не может быть < 0.") #вывод информации о том, что было ввёдено отрицательное число
            continue #продолжение цикла
    except ValueError: #проверка на принадлежности к типу float
        print("Введите число.")
        continue#продолжение цикла
    break #прерывание цикла
for i in range(N):
    while True:
        try:
            a = (float(input("Введите рост ученика:")))
            if a <= 0 or a > 200:  # условие ввода отрицательных чисел
                print("Недоопустимый рост.")  # вывод информации о том, что было ввёдено отрицательное число
                continue  # продолжение цикла
            else:
                test.append(a)
        except ValueError:  # проверка на принадлежности к типу float
            print("Введите число.")
            continue  # продолжение цикла
        break
while True:#цикл для ввода переменной
    try:
        rost = float(input("Введите рост Пети:")) #ввод количества элементов в списке
        if rost <= 0 or rost > 200: #условие ввода отрицательных чисел
            print("Недоопустимый рост.") #вывод информации о том, что было ввёдено отрицательное число
            continue #продолжение цикла
    except ValueError: #проверка на принадлежности к типу float
        print("Введите число.")
        continue#продолжение цикла
    break #прерывание цикла
for j in range(len(test)-1):
    if test[j] > rost > test[j+1]:
        test.insert(j+1,rost)
    if rost == test[j]:
        test.remove(test[j])
        test.insert(j,rost)
if rost < min(test):
    test.append(rost)
if rost > max(test):
    test.insert(0,rost)
print("Петя должен стать в строй под номером:", test.index(rost)+1)
print(input("Нажмите клавишу \"Enter\" для окончания работы программы"))  # Команда для окончания программы