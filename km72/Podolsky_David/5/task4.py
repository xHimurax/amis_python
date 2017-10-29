print('Задание 5.4')
print('Программа выводит первые два элемента, которые одного знака')
while True:
 list1=str(input('Введите список: '))
 list1=list1.split()
 for i in range(0, len(list1)):
  	if (int(list1[i])<=0 and int(list1[i+1])<=0) or (int(list1[i])>=0 and int(list1[i+1])>=0):
  		print (list1[i], list1[i+1])
  		break
  	else:
  		break
