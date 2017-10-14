first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

print()     #JUST an INDENT

if first_number == second_number:
    if second_number == third_number:
        print(3)
    else:
        print(2)
elif second_number == third_number:
    print(2)
elif first_number == third_number:
    print(2)
else:
    print(0)
