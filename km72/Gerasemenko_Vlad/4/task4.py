a = int(input("Введіть рік:"))
if (a%100!=0) and (a // 4):
    print("Leap")
if (a//400):
    print("Leap")
else:
    print("Common")
