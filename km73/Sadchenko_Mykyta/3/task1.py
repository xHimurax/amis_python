print("Вітаємо!\nЦя програма виконує суму 3-х чисел.\n")

import time
time.sleep(2)

while True:
    try:
        a = float(input("Введіть число A: "))
        break
    except Exception:
        print("Недопустимий формат\n")
        continue

while True:
    try:
        b = float(input("Введіть число B: "))
        break
    except Exception:
        print("Недопустимий формат\n")
        continue

while True:
    try:
        c = float(input("Введіть число C: "))
        break
    except Exception:
        print("Недопустимий формат\n")
        continue

s = float(a+b+c)

time.sleep(1)

print("\nСума:",s)
