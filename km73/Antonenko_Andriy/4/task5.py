
first_number = int(input("Введіть перше число : "))
second_number = int(input("Введіть друге число : "))
third_number = int(input("Введіть третє число : "))
if first_number == second_number ==third_number:
    answer = 3
else:
    if first_number == second_number or first_number == second_number or second_number == third_number:
      answer = 2
    else:
      answer = 0

print(answer)