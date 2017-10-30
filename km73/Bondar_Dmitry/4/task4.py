year = int(input("Please enter year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    answer = "LEAP"
else:
    answer = "COMMON"
print(answer)
input()





