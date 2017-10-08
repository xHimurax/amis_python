print("Вітаємо!\nЦя програма рахує необхібну кількість столів для учнів 3-х класів.\n")

import time
time.sleep(2)

while True:
    try:
        k1 = int(input("Введіть кількість учнів 1-ї групи: "))
        if k1<=0:
            print("Потрібно додатнє число\n")
            time.sleep(1)
            continue
        break
    except Exception:
        print("Неправильний формат\n")
        time.sleep(1)
        continue

while True:
    try:
        k2 = int(input("Введіть кількість учнів 2-ї групи: "))
        if k2<=0:
            print("Потрібно додатнє число\n")
            time.sleep(1)
            continue
        break
    except Exception:
        print("Неправильний формат\n")
        time.sleep(1)
        continue

while True:
    try:
        k3 = int(input("Введіть кількість учнів 3-ї групи: "))
        if k3<=0:
            print("Потрібно додатнє число\n")
            time.sleep(1)
            continue
        break
    except Exception:
        print("Неправильний формат\n")
        time.sleep(1)
        continue

tab1 = (k1//2)+(k1%2) 
tab2 = (k2//2)+(k2%2)
tab3 = (k3//2)+(k3%2)
tab = tab1+tab2+tab3  #кількість столів

time.sleep(1)

print("\nНеобхідна кількість столів:",tab)


