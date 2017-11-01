first_number = int(input('enter firs number:',))
second_number = int(input('enter second number:',))
third_number = int(input('enter third number:',))
if (first_number < second_number) & (first_number < third_number):
    print('first number is least')
elif (first_number > second_number) & (third_number > second_number):
    print('second number is least')
else:
    if (third_number < second_number) & (third_number < first_number):
        print('third number is least')
