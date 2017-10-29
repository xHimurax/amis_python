print('Задание 5.7')
print('Программа выводит количество элементов, которые больше своих соседей')
while True:
 list1=str(input('Введите список: '))
 list1=list1.split()
 for i in range(0, len(list1)):
  if list1[len(list1)-1]>list1[i]:
  	n=i+1
  	break
  elif list1[len(list1)-1]==list1[i]:
  	n=i+1
 print(n)
