y = int(input("Enter year: "))

if (y % 400 == 0) | ((y % 100 != 0)&(y % 4 == 0)):
    result = "LEAP"
else:
    result = "COMMON"

print(result)
