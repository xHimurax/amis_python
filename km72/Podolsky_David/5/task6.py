print('Задание 5.6')
print('Программа выводит максимальный элемент и его порядок')
while True:
 list1=str(input('Введите список: '))
 list1=list1.split()
 max=list1[0]
 number=0
 for i in range(1, len(list1)):
 	if max<list1[i]:
 		max=list1[i]
 		number=i
 print(max, number)
