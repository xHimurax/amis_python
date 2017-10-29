import math
print("Добро пожаловать")
while True:
 while True:
   try:
     x=int(input("Введіть число="))
     break
   except ValueError:
     print("Введіть числове значення")
 hours=x//60
 minutes=x%60
 print("Час", round(hours%24),":",round(minutes))
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
    
