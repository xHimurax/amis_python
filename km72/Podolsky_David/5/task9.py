print('Задание 5.9')
print('Программа переставляет соседние элементы')
while True:
 list1=str(input('Введите список: '))
 list1=list1.split()
 print(list1)
 newlist=''
 for i in range(0, len(list1)-1):
 	if i%2==0:
 		newlist=newlist+list1[i+1]
 	elif not(i%2==0):
 		newlist=newlist+list1[i-1]
 if len(list1)%2==0:
  newlist=newlist+list1[len(list1)-2]
 else:
  newlist=newlist+list1[len(list1)-1]
 print(newlist)
