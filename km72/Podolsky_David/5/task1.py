print('Задание 5.1')
print('Программа выводит элементы чётных индексов')
while True:
 list1=str(input('Введите список: '))
 list1=list1.split()
 i=0
 while i in range(0, len(list1)):
	 print(list1[i])
	 i=i+2
