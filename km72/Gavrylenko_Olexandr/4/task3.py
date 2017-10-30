first_number = int(input('Enter 1st number:'))
second_number = int(input('Enter 2nd number:'))
third_number = int(input('Enter 3rd number:'))
if first_number<second_number and third_number:
    print(first_number)
elif second_number<first_number and third_number:
    print(second_number)
elif third_number<first_number and second_number:
    print(third_number)
