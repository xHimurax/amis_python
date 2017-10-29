import math
print("Добро пожаловать")
while True:
 while True:
   try:
     x=int(input("Введіть число="))
     break
   except ValueError:
     print("Введіть числове значення")
 print("The next number for the number",x,"is",x+1)
 print("The previous number for the number",x,"is",x-1)
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
    
