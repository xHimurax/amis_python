first_x = int(input('Введіть поточний номер рядка фігури : '))
first_y = int(input('Введіть поточний номер стовпця фігури : '))
second_x = int(input('Введіть номер рядка кінцевої клітинки : '))
second_y = int(input('Введіть номер стовпця кінцевої клітинки '))
if first_y > 8 or first_x > 8 or second_y > 8 or second_x > 8:
    answer = 'Кордината не може перевищувати 8'
else:
    if (abs(first_x - second_x) ==1 and abs(first_y-second_y)==1) or \
            (abs(first_x - second_x)==1 and first_y==second_y) or (abs(first_y-second_y)==1 and first_x==second_x):
        answer = "YES"
    else:
        answer = "NO"

print(answer)