'''
Умова: Дано три цілих числа. Вивести найменше з них.

Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести ціле число
'''
a = int(input("Введіть перше число - "))
b = int(input("Введіть друге число - "))
c = int(input("Введіть третє число - "))
if a>b:
    mina = b
elif a<b:
    mina = a
else:
    mina = a
if c>mina:
    mine = mina
elif c<mina:
    mine = c
else:
    mine = c
print(mine)
