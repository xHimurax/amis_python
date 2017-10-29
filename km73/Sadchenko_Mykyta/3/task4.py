print("Вітаємо!\nЦя програма визначає кількість яблук на одного студента.\n")

import time
time.sleep(2)

while True:
    try:
        n = int(input("Введіть кількість студентів: "))
        if n<0:
            print("Потрібно натуральне число\n")
            time.sleep(1)
            continue
        elif n==0:
            print("На нуль не ділиться :(\n")
            time.sleep(1)
            continue
        break
    except Exception:
        print("Недопустимий формат\n")
        time.sleep(1)
        continue

while True:
    try:
        k = int(input("Введіть кількість яблук: "))
        if k<0:
            print("Потрібно натуральне число\n")
            time.sleep(1)
            continue
        elif k==0:
            print("На нуль не ділиться :(\n")
            time.sleep(1)
            continue
        break
    except Exception:
        print("Недопустимий формат\n")
        time.sleep(1)
        continue

if k>=n:
    podil = int(k//n)
    ost = int(k%n)
    time.sleep(1)
    print("\nКількість яблук на одного студента:",podil)
    print("Яблука, що лишилися в кошику:",ost)
else:
    time.sleep(1)
    print("\nКількість яблук на одного студента: 0")
    print("Яблука, що лишилися в кошику:",k)

