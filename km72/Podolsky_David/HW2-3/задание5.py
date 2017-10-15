import time
print('Задание №5')
print('               Добро пожаловать. \nДанная программа считает z+1 и z-1, где z - целлое число')
while True:
 while True:
  try:
   z=int(input('Введите z='))
   break
  except ValueError:
  	print('z должно быть целым числом')
 print('После числа ',z,' идёт ',z+1)
 print('Перед числом ',z,' идёт ',z-1)
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
