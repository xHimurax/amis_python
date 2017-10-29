print("Добро пожаловать")
while True:
 while True:
   try:
     n=int(input("Введіть n="))
     break
   except ValueError:
     print("Введіть число")
 while True:
    try:
      m=int(input("Введіть m="))
      break
    except ValueError:
     print("Введіть число")
 while True:
    try:
      k=int(input("Введіть k="))
      break
    except ValueError:
     print("Введіть число")
 if m%2==0 or n%2==0:
     print("yes")
 else:
     print("no")
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
    
