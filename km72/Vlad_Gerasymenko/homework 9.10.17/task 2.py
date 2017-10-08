while True:
    try:
        a = float(input("Введіть довжину першого катету:"))
    except ValueError:
        print("Ви ввели не число!")
        continue
    try:
        b = float(input("Введіть довжину другого катету:"))
    except ValueError:
        print("Ви ввели не число!")
        continue
    print("S=",((a*b)/2))
