'''
Умова: Вивести результат функції sign(x), що визначається наступним чином: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0..

Вхідні дані: користувач вводить дійсне число.

Вихідні дані: вивести результат sign.
'''
x = float(input(' x = '))
if x>0:
    answer = 1
elif x<0:
    answer = -1
else:
    answer = 0
print('sign(x)', '=', answer)
