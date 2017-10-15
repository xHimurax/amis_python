def inp_ut(x):
     while True :
         try :
             text = '{} {} {} '.format("Введите",x,'>>>')
             a = int(input(text))
             return a
         except ValueError :
             print("Введите число")
while True :
  
     AB = float(input("Длина первого катета: ")) 
     AC = float(input("Длина второго катета: ")) 
     S = (AB * AC) / 2 
     print("Площадь треугольника: %.2f" % S)     
     if input("Try again?") == "no":
         break
