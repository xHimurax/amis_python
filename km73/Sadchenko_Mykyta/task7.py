print("Вітаємо!\nЦя програма виводить час на екран за заданну кількість хвилин.\n")

import time
time.sleep(2)

while True:
    try:
        allMins = int(input("Введіть кількість хвилин: "))
        if allMins<0:
            print("Потрібно додатнє число\n")
            time.sleep(1)
            continue
        break
    except Exception:
        print("Неправильний формат\n")
        time.sleep(1)
        continue

hours = (allMins//60)%24
mins = allMins%60

time.sleep(1)

print("\nПоточний час - ",hours,":",mins)
