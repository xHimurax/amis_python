print("Enter year")
x=int(input())
if (((x%4==0) and ((x%100)!=0)) or (x%400==0)):
    answer="LEAP"
else:
    answer="COMMON"
print(answer)
