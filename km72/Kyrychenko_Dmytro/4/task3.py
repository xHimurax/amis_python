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

 if x<y and x<z:
     print ("x =",x)
 elif y<x and y<z:
     print ("y =",y)
 elif z<x and z<y:
     print ("z =",z)
 elif x==y or z==y or z==x:
     print ("найменшого немає")

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
    
