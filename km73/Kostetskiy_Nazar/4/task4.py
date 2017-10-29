x = int(input("Enter year: "))

if (x/4 == x//4) and (x/100 != x//100):

    answer = "LEAP"

elif (x/400 == x//400):
    answer = "LEAP"

else:

    answer = "COMMON"
print("My answer is:",answer)
input()