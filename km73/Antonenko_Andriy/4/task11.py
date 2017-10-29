
first_x = int(input('Введіть поточний номер рядка фігури : '))
first_y = int(input('Введіть поточний номер стовпця фігури : '))
second_x = int(input('Введіть номер рядка кінцевої клітинки : '))
second_y = int(input('Введіть номер стовпця кінцевої клітинки :'))
if first_y > 8 or first_x > 8 or second_y > 8 or second_x > 8:
    answer = 'Кордината не може перевищувати 8'
else:
    a = first_x+first_y
    b = second_x+second_y
    if abs(a-b)==1 or abs(a-b)==3:
        answer = "YES"
    else:
        answer = "NO"

print(answer)