y=int(input("Enter the year: "))
if y%4==0 and y%100!=0:    
    print("LEAP")
elif y%400==0:
    print("LEAP")
else:
    print("COMMON")
input()
