import math
print("Добро пожаловать")
while True:
 x=input("Введіть ваше ім'я=")
 print("Hello,", x,"!")    
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
    
