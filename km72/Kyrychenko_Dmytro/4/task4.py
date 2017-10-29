print("Добро пожаловать")
while True:
 while True:
   try:
     x=int(input("Введіть рік="))
     break
   except ValueError:
     print("Введіть число")
 if x%4==0 and x%100!=0:
     print("LEAP")
 else:
     print("COMMON")



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
    
