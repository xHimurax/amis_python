print("Добро пожаловать")
while True:
 while True:
   try:
     x=float(input("Введіть x="))
     break
   except ValueError:
     print("Введіть число")
 while True:
    try:
      y=float(input("Введіть y="))
      break
    except ValueError:
     print("Введіть число")
 while True:
    try:
      z=float(input("Введіть z="))
      break
    except ValueError:
     print("Введіть число")
 print("x+y+z=",float(x+y+z))
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
    
