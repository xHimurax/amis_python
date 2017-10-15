def inp_ut(x):
    while True :
        try :
            text = '{} {} {} '.format("Введите количество ",x,'>>>')
            a = int(input(text))
            return a
        except ValueError :
            print("Введите число")
while True: 
    minutes = int(input("Enter a minutes, please: ")) 
    hours = int(minutes/60) 
    minutes %= 60 
    print ("Time from midnight ",hours,":",minutes) 
    if input("Try again? ") == "no": 
        break 
