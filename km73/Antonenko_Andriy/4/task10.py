first_x = int(input('Введіть поточний номер рядка фігури : '))
first_y = int(input('Введіть поточний номер стовпця фігури : '))
second_x = int(input('Введіть номер рядка кінцевої клітинки : '))
second_y = int(input('Введіть номер стовпця кінцевої клітинки :'))
if first_y > 8 or first_x > 8 or second_y > 8 or second_x > 8:
    answer = 'Кордината не може перевищувати 8'
else:
    k = (first_x + first_y) % 2
    l = (second_x + second_y) % 2
if first_x == second_x or first_y == second_y\
            or (k == l and first_y==first_x and second_y==second_x) or (k==l and first_x+first_y == second_x+second_y) or\
        (abs((first_y+first_x)-(second_y+second_x))%2 == k):
    answer = 'YES'
else:
    answer = 'NO'

print(answer)