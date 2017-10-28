while True:
    try:
        g1 = int(input("Введіть кількість учнів в 1 групі:"))
    except ValueError:
        print("Ви ввели не ціле число!")
        continue
    try:
        g2 = int(input("Введіть кількість учнів в 2 групі:"))
    except ValueError:
        print("Ви ввели не ціле число!")
        continue
    try:
        g3 = int(input("Введіть кількість учнів в 3 групі:"))
    except ValueError:
        print("Ви ввели не ціле число!")
        continue
    s1 = g1//2
    s2 = g2//2
    s3 = g3//2
    print("Необхідне число столів:",(s1+s2+s3))
