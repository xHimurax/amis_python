while True:
    try:
        N = int(input("Введіть кількість студентів:"))
    except ValueError:
        print("Ви ввели не ціле число!")
        continue
    try:
        K = int(input("Введіть кількість яблук:"))
    except ValueError:
        print("Ви ввели не ціле число!")
        continue
    print("Кожен студент отримав по",(K//N),"яблук(a)")
    print("В кошику залишилось",(K%N),"яблук(а)")
