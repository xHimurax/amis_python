x1 = int(input("введите первую координату первой клетки (от 1 до 8) - "))
y1 = int(input("введите вторую координату первой клетки (от 1 до 8) - "))
x2 = int(input("введите первую координату второй клетки (от 1 до 8) - "))
y2 = int(input("введите вторую координату второй клетки (от 1 до 8) - "))
import math
if x1 == x2:
    ans = "YES"
elif y1 == y2:
    ans = "YES"
elif (abs(x1 - y1) == abs(x2 - y2)):
    ans = "YES"
elif ((x1 + 1) >= x2 >= (x1 - 1))&((y1 + 1) >= y2 >= (y1 - 1)):
    ans = "YES"
else:
    ans = "NO"
print(ans)
input()
