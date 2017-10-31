a = int(input("Введите первое число - "))
b = int(input("Введите второе число - "))
c = int(input("Введите третье число - "))
if a == b:
    if a == c:
        ans = 3
    else:
        ans = 2
elif b == c:
    ans = 2
elif a == c:
    ans = 2
else:
    ans = 0
print("Количество одинаковых чисел -",ans)
input()
