def inp_ut(x):
    while True :
        try :
            text = '{} {} {} '.format("Введите количество ",x,'>>>')
            a = int(input(text))
            return a
        except ValueError :
            print("Введите число")
while True :

    N = inp_ut("студентов:")
    K = inp_ut("яблук:")

    appleForStudent = K // N
    appleInBag = K % N
    print("Сколько яблок на студента",appleForStudent)
    print("Сколько яблок в ящике",appleInBag)    
  
    if input("Try again?") == "no":
        break
     