def inp_ut(x):
    while True :
        try :
            text = '{} {} {} '.format("Введите значения ",x,'>>>')
            a = float(input(text))
            return a
        except ValueError :
            print("Введите число")
           

while True :
 
    x = inp_ut("первого числа")
    y = inp_ut("второго числа")
    z = inp_ut("третьего числа")

    sum = x + y + z 
    
    print("Сума чисел равна",sum)

    if input("Try again?") == "no":
        break
