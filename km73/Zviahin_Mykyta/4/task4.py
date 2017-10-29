year = int(input("Enter a year: "))

if (((year % 4) == 0) & ((year % 100) != 0)) or (year % 400) == 0:
    print("The year is leap")

else:
    print("The year is common")

input()

