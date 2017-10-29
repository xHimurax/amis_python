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
 if x<y:
     print ("x=",x)
 elif y<x:
     print ("y=",y)
 else:
     print ("x=y")

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
    
