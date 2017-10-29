print("Добро пожаловать")
while True:
 while True:
     x1=int(input("Введіть x1="))
     if x1>=1 and x1<=8:
        break
     else:
         continue
 while True:
     y1=int(input("Введіть y1="))
     if x1>=1 and x1<=8:
        break
     else:
         continue
 while True:
     x2=int(input("Введіть x2="))
     if x1>=1 and x1<=8:
        break
     else:
         continue
 while True:
     y2=int(input("Введіть y2="))
     if x1>=1 and x1<=8:
        break
     else:
         continue
 if x1%2==0 and y1%2==0 and x2%2==0 and y2%2==0:
     print("yes")
 elif x1%2!=0 and y1%2==0 and x2%2!=0 and y2%2==0:
     print("yes")
 elif x1%2==0 and y1%2!=0 and x2%2==0 and y2%2!=0:
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
    
