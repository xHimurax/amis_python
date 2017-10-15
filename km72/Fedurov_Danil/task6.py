def inp_ut(x):
    while True :
        try :
            text = '{} {} {} '.format("Сколько учеников в",x,'>>>')
            a = int(input(text))
            return a
        except ValueError :
            print("Введите число")
           

while True :
    
    x = inp_ut("первой группе:")
    y = inp_ut("второй группе:")
    z = inp_ut("третьей группе:")
    sum = x + y + z
    tableOn3Groups = sum // 2
    if sum % 2 == 1:
        tableOn3Groups += 1
        
    print("Мінімальну кількість столів необхідно придбати:",tableOn3Groups)
    


    if input("Try again?") == "no":
        break
