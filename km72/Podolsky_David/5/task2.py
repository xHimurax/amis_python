print('Задание 5.2')
print('Программа выводит чётные элементы списка')
while True:
 list1=str(input('Введите список: '))
 list1=list1.split()
 for i in range(0, len(list1)):
 	if (int(list1[i]))%2==0:
 		print(list1[i])
