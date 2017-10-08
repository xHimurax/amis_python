print("Вітаємо!\nЦя програма друкує сусідні цілі числа введеного значення.\n")

import time
time.sleep(2)

while True:
    try:
        num = int(input("Введіть номер: "))
        break
    except Exception:
        print("Неправильний формат\n")
        time.sleep(1)
        continue

nextNum = int(num+1)
prevNum = int(num-1)

time.sleep(1)
print("\nНаступне число значення '",num,"' - це '",nextNum,"'")
print("Минуле число значення '",num,"' - це '",prevNum,"'") 




                  
