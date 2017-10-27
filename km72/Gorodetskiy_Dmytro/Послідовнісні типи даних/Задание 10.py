test = []
while True:#цикл для ввода переменной
    try:
        N = int(input("Введите количество элементов списка:")) #ввод количества элементов в списке
        if N <= 0: #условие ввода отрицательных чисел
            print("Количество элементов не может быть < 0.") #вывод информации о том, что было ввёдено отрицательное число
            continue #продолжение цикла
    except ValueError: #проверка на принадлежности к типу float
        print("Введите число.")
        continue#продолжение цикла
    break #прерывание цикла
for i in range(N):
    while True:
        try:
            a = (int(input("Введите ваше число:")))
            test.append(a)
        except ValueError:  # проверка на принадлежности к типу float
            print("Введите число.")
            continue  # продолжение цикла
        break
"""a = test.index(min(test))
b = test.index(max(test))
test.insert(a, max(test))
test.insert(b+1, min(test))
del test[max(test)+1]
del test[min(test)]"""
print(test)

