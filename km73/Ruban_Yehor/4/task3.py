a = float(input("Введите первое число - "))
b = float(input("Введите второе число - "))
c = float(input("Введите третье число - "))
if a < b:
    if a < c:
        ans = a
    else:
        ans = c
else:
    if b < c:
        ans = b
    else:
        ans = c
print("Наименьшее число - ",ans)
input()
