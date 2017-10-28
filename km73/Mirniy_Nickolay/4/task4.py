year = int(input('Number of year : '))
a = year//400
b = year//4

if (a == True) or (b == True) :
    answer = "LEAP"
else :
    answer = "COMMON"
print(answer)
