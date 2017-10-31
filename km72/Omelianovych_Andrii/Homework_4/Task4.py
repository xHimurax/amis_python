year = int(input('Year: '))
if not (year%4) and (year%100) or not (year%400):
    typeofyear = "LEAP"
else:
    typeofyear = "COMMON"
print(typeofyear)
