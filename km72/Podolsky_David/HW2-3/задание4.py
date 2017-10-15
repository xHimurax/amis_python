import time
print('Задание №4')
print('               Добро пожаловать. \n  Данная программа распределяет яблоки между \nстудентами и считает, сколько останется в корзине')
while True:
 
 while True:
  try:
   k=int(input('Введите количество яблок '))
  except ValueError:
  	print('Это должно быть натуральное число')
  	continue
  if k<=0:
   print('Это должно быть натуральное число')
  else:
  	break
  	
 while True:
  try:
   n=float(input('Введите количество студентов '))
  except ValueError:
  	print('Это должно быть натуральное число')
  	continue
  if n<=0:
   print('Это должно быть натуральное число')
  else:
  	break
  	
 x=k//n
 y=k%n
 
 print('На одного студента ',x,' яблок')
 print('В корзине осталось ',y,' яблок')
 
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
