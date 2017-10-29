
num_first = int(input("Введіть кількість учнів першої групи: "))
num_sec = int(input("Введіть кількість учнів другої групи: "))
num_third = int(input("Введіть кількість учнів третьої групи: "))

if num_first%2 == 0:
    a = num_first//2
if num_first%2 == 1:
    a = (num_first//2) + 1

if num_sec%2 == 0:
    b = num_sec//2
if num_sec%2 == 1:
    b = (num_sec//2) + 1

if num_third%2 == 0:
    c = num_third//2
if num_third%2 == 1:
    c = (num_third//2) + 1

print("Всього необхідно парт: " + str(a + b + c))
