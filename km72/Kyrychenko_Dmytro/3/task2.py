import math
print("Добро пожаловать")
while True:
 while True:
   try:
     x=float(input("Введіть перший  катет="))
     break
   except ValueError:
     print("Введіть число")
 while True:
    try:
      y=float(input("Введіть другий катет="))
      break
    except ValueError:
     print("Введіть число")
 print("Площа трикутника=",float((x*y)/2))    
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
    
