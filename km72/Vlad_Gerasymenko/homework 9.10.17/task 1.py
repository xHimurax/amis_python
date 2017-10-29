while True:
    try:
        a = float(input("Введіть а:"))
    except ValueError:
        print("Ви ввели не число")
        continue
    try:
        b = float(input("Введіть b:"))
    except ValueError:
        continue
        print("Ви ввели не число")
    try:
        c = float(input("Введіть с:"))
    except ValueError:
        print("Ви ввели не число")
        continue
        print("Ви ввели не число")
    print("a+b+c=",(a+b+c))
