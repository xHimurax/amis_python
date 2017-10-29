a=int(input("Введіть кількість хвилин: "))

result = "Поточний час дорівнює: " + str((a%1440)//60).zfill(2) + ":" + str((a%1440)%60).zfill(2)

print(result)
