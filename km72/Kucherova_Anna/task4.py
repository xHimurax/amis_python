x = int(input("Enter year: "))

if (x % 4 == 0) & (x % 100 !=0):
    print("LEAP")
elif (x % 400 == 0):
    print("LEAP")
else:
    print("COMMON")

