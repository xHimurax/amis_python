x=int(input("Введіть число a: "))
if (x%4)==0 and (x%100)!=0 or (x%400)==0:
    print("LEAP")
else:
    print("COMMON")
