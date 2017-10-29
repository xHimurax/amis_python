print("Вітаємо!\nЦя програма знаходить площу прямокутного трикутника за катетами.\n")

import time
time.sleep(2)

while True:
    try:
        k1 = float(input("Введіть довжину 1-го катета: "))
        break
    except Exception:
        print("Недопустимий формат\n")
        continue

while True:
    try:
        k2 = float(input("Введіть довжину 2-го катета: "))
        break
    except Exception:
        print("Недопустимий формат\n")
        continue

s = float((k1+k2)/2)

time.sleep(1)

print("\nПлоща:", s)
