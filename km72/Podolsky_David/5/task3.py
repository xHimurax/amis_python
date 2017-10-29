print('Задание 5.3')
print('Программа выводит элементы списка которые больше предыдущего')
while True:
 list1=str(input('Введите список: '))
 list1=list1.split()
 for i in range(0, len(list1)):
 	  if list1[i]>list1[i-1]:
 	   print(list1[i])
