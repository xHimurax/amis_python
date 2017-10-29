print('Задание 5.14')
print('Программа выводит уникальные элементы')
while True:
 a=input('\nВведите список: ').split()
 count=-1
 for i in a:
  for b in a:
   if i == b:
    count=count+1
  if count==0:
   print(i, end=' ')
  count=-1
