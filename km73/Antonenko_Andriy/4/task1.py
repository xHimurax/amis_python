
first_number = int(input('Введіть перше число : '))
second_number = int(input('Введіть друге число : '))

if first_number<second_number:
    answer = first_number
if second_number<first_number:
    answer = second_number
if second_number == first_number:
    answer = 'Числа рівні'

print (answer)