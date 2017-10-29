print('Задание 5.5')
print('Программа выводит количество элементов, которые больше своих соседей')
while True:
 list1=str(input('Введите список: '))
 list1=list1.split()
 newlist=''
 for i in range(0, len(list1)):
  if list1[i]>list1[i-1] and list1[i]>list1[i+1]:
   newlist=newlist+list1[i]
 print(len(newlist))
