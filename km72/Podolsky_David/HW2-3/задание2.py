import time
print('Задание №2')
print('               Добро пожаловать. \nДанная программа находит площадь прямоугольного \n       треугольника за двумя катетами')
while True:
	
 while True:
  try:
   a=float(input('Введите первый катет = '))
  except ValueError:
  	print('Катет должен быть числом')
  	continue
  if a<=0:
   print('Сторона не может быть отрицательной')
  else:
  	break

 while True:
  try:
   b=float(input('Введите второй катет = '))
  except ValueError:
  	print('Катет должен быть числом')
  	continue
  if b<=0:
   print('Сторона не может быть отрицательной')
  else:
  	break
 print('Площадь треугольника =', a*b/2)
 
 while True:
     answer = input('Повторить программу? (да или нет): ')
     if answer in ('да', 'нет'):
         break
     print ('Введите да или нет')
 if answer == 'да':
     continue
 else:
     print ('Программа окончена')
     time.sleep(3)
     break
     exit()
