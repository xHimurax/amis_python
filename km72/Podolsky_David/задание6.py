import time
print('Задание №6')
print('               Добро пожаловать. \nДанная программа считает сколько нужно столов на класс')
while True:

 while True:
  try:
   k1=int(input('Введите количество учеников в первой группе '))
  except ValueError:
  	print('Это должно быть натуральное число')
  	continue
  if k1<=0:
   print('Это должно быть натуральное число')
  else:
  	break
  	
 while True:
  try:
   k2=int(input('Введите количество учеников во второй группе '))
  except ValueError:
  	print('Это должно быть натуральное число')
  	continue
  if k2<=0:
   print('Это должно быть натуральное число')
  else:
  	break
  	
 while True:
  try:
   k3=int(input('Введите количество учеников в третьей группе '))
  except ValueError:
  	print('Это должно быть натуральное число')
  	continue
  if k3<=0:
   print('Это должно быть натуральное число')
  else:
  	break
  	
 x=k1+k2+k3//2
 y=(k1+k2+k3)%2
 print('Необходимо купить ',x+y,' столов')
 
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
