print('Задание №7')
print('               Добро пожаловать. \nДанная программа переводит количество минут в формат Ч:М')
while True:
 
 while True:
  try:
   n=int(input('Введите количество минут '))
  except ValueError:
  	print('Это должно быть натуральное число')
  	continue
  if n<=0:
   print('Это должно быть натуральное число')
  else:
  	break
  	
 while n>1439:
 	n=n-1440
 
 x=n//60
 y=n%60
 
 print(x,':',y)
 
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
