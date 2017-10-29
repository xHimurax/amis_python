a=int(input("Введiть початковий рядок (1-8):")) #Початковий рядок
b=int(input("Введiть початковий стовпчик (1-8):")) #Початковий стовпчик
af=int(input("Введiть кiнцевий рядок (1-8):")) #Кінцевий рядок
bf=int(input("Введiть кiнцевий стовпчик (1-8):")) #Кінцевий стовпчик
if a<0 or a>8 or b<0 or b>8 or af<0 or af>8 or b<0 or bf>8:
    print("No data")
elif a==af or b==bf:
    print("Yes")
else:
    print("No")
input("\n\nPress Enter to exit the program.")
