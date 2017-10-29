
first_number = int(input('Введіть ціле число : '))
second_number = int(input('Введіть ціле число : '))
third_number = int(input('Введіть ціле число : '))
if first_number==second_number==third_number:
    answer = 'Числа рівні'
else:
    if first_number<second_number and first_number<third_number:
      answer = str(first_number)
    else:
      if second_number<first_number and second_number<third_number:
        answer = str(second_number)
      else:
        if third_number<second_number and third_number<first_number:
            answer = str(third_number)


print(answer)
