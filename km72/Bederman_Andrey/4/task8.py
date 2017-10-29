a=int(input("Введiть рядок для 1 клiтинки (1-8):")) 
b=int(input("Введiть стовпчик для 1 клiтинки (1-8):")) 
af=int(input("Введiть рядок для 2 клiтинки (1-8):")) 
bf=int(input("Введiть стовпчик для 2 клiтинки (1-8):")) 
if a<0 or a>8 or b<0 or b>8 or af<0 or af>8 or b<0 or bf>8:
    print("no data")
elif abs(a-b)<=1 and abs(af-bf)<=1:
    print("YES")
else:
    print("NO")
input("\n\nPress Enter to exit the program.")
