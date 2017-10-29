print('Задание 5.10')
print('Программа переставляет min и max')
while True:
 list1=str(input('Введите список: '))
 list1=list1.split()
 
 max=list1[0]
 number1=0
 for i in range(1, len(list1)):
 	if max<list1[i]:
 		max=list1[i]
 		number1=i

 min=list1[0]
 number2=0
 for i in range(1, len(list1)):
 	if min>list1[i]:
 		min=list1[i]
 		number2=i
 		
 list1[number1]=min
 list1[number2]=max
 print(list1)
