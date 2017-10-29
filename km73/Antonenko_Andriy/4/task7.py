
x = int(input('Введіть номер рядка : '))
y = int(input('Введіть номер стовпця : '))
if x>8 or y>8:
    answer = 'Координата не може перевищувати 8'
else:
    a = (x+y)%2
    if a == 0:
        answer = 'YES'
    else:
        answer = 'NO'
print(answer)
