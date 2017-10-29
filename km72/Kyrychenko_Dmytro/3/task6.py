import math
print("Добро пожаловать")
while True:
 while True:
   try:
     x=int(input("Введіть кількість учнів в першому класі="))
     break
   except ValueError:
     print("Введіть число")
 while True:
    try:
      y=int(input("Введіть кількість учнів в другому класі="))
      break
    except ValueError:
     print("Введіть число")
 while True:
    try:
      z=int(input("Введіть кількість учнів в третьому класі="))
      break
    except ValueError:
     print("Введіть число")
 print("Кількість столів для першого класу",int(x//2+x%2))
 print("Кількість столів для другого класу",int(y//2+y%2))
 print("Кількість столів для третього класу",int(z//2+z%2))
 while True:
   answer = input("Повторити чи вийти?(п чи в)")
   if answer in ("п", "в"):
      break
   print ("Введіть п чи в")
 if answer == "п":
   continue
 else:
   print("Кінець")
   exit()
    
