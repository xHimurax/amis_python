import time
print('Задание №1')
print('               Добро пожаловать. \nДанная программа решает уравнение вида: a+b+c')
while True:
	
 while True:
  try:
   a=float(input('Введите a='))
   break
  except ValueError:
  	print('a должно быть числом')
  	
 while True:
  try:
   b=float(input('Введите b='))
   break
  except ValueError:
  	print('b должно быть числом')
  	
 while True:
  try:
   c=float(input('Введите c='))
   break
  except ValueError:
  	print('c должно быть числом')
  	
 print('a+b+c=', a+b+c)
 
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
