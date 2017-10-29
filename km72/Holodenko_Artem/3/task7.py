import time
a=int(input("Введіть кількість хвилин: "))
a=a%1440
h=a//60
m=a%60
print("Результат:",h,":",m)
time.sleep(3)
