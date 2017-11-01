first_of_the_year = int(input('please enter the year:',))
if first_of_the_year % 4 == 0:
    print('LEAP')
elif first_of_the_year % 100 == 0:
        print('LEAP')
elif first_of_the_year % 400 == 0:
    print("LEAP")
else:
    print('COMMON')
