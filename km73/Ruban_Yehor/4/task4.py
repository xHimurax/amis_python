a = int(input("Введите год - "))
if a % 4 == 0:
    if a % 100 != 0:
        ans = "год высокосный"
    else:
        ans = "год не высокосный"
elif a % 400 == 0:
    ans = "год высокосный"
else:
    ans = "год не высокосный"
print(ans)
input()
