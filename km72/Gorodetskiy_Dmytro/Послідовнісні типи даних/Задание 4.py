test = []#создаём пустой список, в который будут заноситься введённые элементы
while True:#цикл для ввода переменной
    try:
        N = int(input("Введите количество элементов в списке:")) #ввод количества элементов в списке
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
            test.append(float(input("Введите элемент:")))
        except ValueError:  # проверка на принадлежности к типу float
            print("Введите число.")
            continue  # продолжение цикла
        break
list = []
for j in range(len(test)-1):
    if (int(test[j])<0 and int(test[j+1])<0) or (int(test[j])>0 and int(test[j+1]))>0 :
        list.append(test[j])
        list.append(test[j+1])
if len(list) >2:
    list = list[0:2]
print("Следующие соседние элементы имеют один знак:", list)
print(input("Нажмите клавишу \"Enter\" для окончания работы программы"))  # Команда для окончания программы