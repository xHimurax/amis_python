print("Добро пожаловать")
while True:
 while True:
   try:
     x=float(input("Введіть x="))
     break
   except ValueError:
     print("Введіть число")   


 if x>0:
     print ("sign(x)=1")
 elif x<0:
     print ("sign(x)=-1")
 else:
     print ("sign(x)=0")

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
    
