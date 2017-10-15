n = int(input("Введіть n:"))
m = int(input("Введіть m:"))
k = int(input("Введіть k:"))
mn = str(input("Ви відрізваєте n рядків, чи m стовпчиків?(n/m)"))
if mn == "n":
    if ((m*n)//n):
        print("yes")
    else:
        print("no")
elif mn == "m":
    if ((m*n)//m):
        print("yes")
    else:
        print("no")
else:
    print("Ви не ввели n/m")
