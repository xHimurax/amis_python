while True:
    try:
        N = int(input("Введіть кількість хвилин:"))
    except ValueError:
        print("")
        continue
    hours = N//60
    minutes = N%60
    while hours>24:
        (hours - 24)
    print(hours,":",minutes)
