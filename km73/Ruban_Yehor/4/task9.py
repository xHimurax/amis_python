a1 = int(input("Введите координату X первой клетки - "))
a2 = int(input("Введите координату Y первой клетки - "))
b1 = int(input("Введите координату X второй клетки - "))
b2 = int(input("Введите координату Y второй клетки - "))
import math
if (abs(a1 - b1) == abs(a2 - b2)):
    ans = "YES"
else:
    ans = "NO"
print(ans)
input()
