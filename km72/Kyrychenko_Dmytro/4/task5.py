print("Добро пожаловать")
while True:
 while True:
   try:
     x=int(input("Введіть x="))
     break
   except ValueError:
     print("Введіть число")
 while True:
   try:
     y=int(input("Введіть y="))
     break
   except ValueError:
     print("Введіть число")
 while True:
   try:
     z=int(input("Введіть z="))
     break
   except ValueError:
     print("Введіть число")
 if x==y and y==z:
     print("3")
 elif x==y or y==z or x==z:
     print ("2")
 else:
     print ("0")





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
    
