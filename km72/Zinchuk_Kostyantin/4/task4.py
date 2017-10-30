year=int(input("Enter Year "))
if (year%4==0) and (year%100!=0):
    print("LEAP")
elif (year%400==0) and (year%100==0):
    print("LEAP")
else:
    print("COMMON")
    
