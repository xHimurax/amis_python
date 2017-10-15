def inp_ut(x):
    while True :
        try :
            text = '{} {} {} '.format("Введите",x,'>>>')
            a = int(input(text))
            return a
        except ValueError :
            print("Введите число")
while True :

    a = inp_ut("число:")
    previos = a - 1
    next = a + 1
    print("The next number for the number",next)
    print("The previous number for the number",previos)

    if input("Try again?") == "no":
        break