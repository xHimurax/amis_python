print("                         Задача №2")
#getting variables
print("Введiть значення 2 катетiв по черзi (вiд'ємнi значення вiзьмуться по модулю)")
A = float(input(""))
B = float(input(""))
#MAIN CODE
'''modul'''
if A>=0:
    A=A
else: A=-A
if B>=0:
    B=B
else: B=-B
'''formula'''
X = A*B/2
#output
print("\n", "Площа дорiвнює:", X, "\n")
d=input("Натиснiть Enter для завершення програми")