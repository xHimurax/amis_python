print('Задание 5.8')
print('Программа выводит количество различных элементов')
while True:
 list1=str(input('Введите список: '))
 list1=list1.split()
 n=0
 for i in range(0, len(list1)):
 	if not(list1[i]==list1[i-1]):
 		n=n+1
 if n==0:
 	n=1
 print(n)
