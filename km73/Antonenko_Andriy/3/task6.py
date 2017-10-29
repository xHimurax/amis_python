
first_group = int(input('Введіть кількість учнів першої групи : '))
second_group = int(input('Введіть кількість учнів другої групи : '))
third_group = int(input('Введіть кількість учнів третьої групи : '))

tables = (first_group + second_group + third_group)//2
a = (first_group + second_group + third_group)%2
if a>0 :
    answer =  str(int(tables + 1))
else:
    answer = str(int(tables))
print('Кількість столів: '+answer)

