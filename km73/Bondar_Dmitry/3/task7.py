min = int(input("Введіть кількість хвилин:"))
hour = min//60
min %= 60
hour %= 24
print("Години -" , int(hour) , "Хвилини -" , int(min))
