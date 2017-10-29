import math
print("Добро пожаловать")
while True:
 while True:
   try:
     x=float(input("Введіть кількість студентів="))
     break
   except ValueError:
     print("Введіть число")
 while True:
    try:
      y=float(input("Введіть кількість яблук="))
      break
    except ValueError:
     print("Введіть число")
 print("Яблук на студента=",int(y/x))
 print("Залишилось яблук",int(y%x))
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
    
