first_number = int(input('Enter 1st number:'))
second_number = int(input('Enter 2nd number:'))
third_number = int(input('Enter 3rd number:'))
if first_number == second_number == third_number:
    print(3)
elif first_number == second_number or second_number == third_number or first_number == third_number:
    print(2)
else:
    print(0)