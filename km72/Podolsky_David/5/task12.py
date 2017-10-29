print('Задание 5.12')
print('Программа вставляет элемент')
while True:
 a=input('Введите список целых чисел: ').split()
 k=int(input('Введите индекс k: '))
 c=input('Введите значение C: ')

 a=" ".join(a[:k]) + " " + c + " " + " ".join(a[k:])
 print(a)
