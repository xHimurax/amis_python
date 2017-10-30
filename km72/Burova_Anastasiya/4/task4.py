year = int(input("Enter year:"))
if not (year%4) and (year%100) or not (year%400):
    type = "LEAP"
else:
    type = "COMMON"
print(type)
