mass = []
for i in range(8):
    mass.append(int(input("Введите координату по Х - ")))
    mass.append(int(input("Введите координату по Y - ")))
import math
for k in mass:
    if mass[k] == mass[k+2]:
        ans = "YES"
    elif mass[k+1] == mass[k+3]:
        ans = "YES"
    elif (abs(mass[k] - mass[k+1])) == (abs(mass[k+2] - mass[k+3])):
        ans = "YES"
    elif ((mass[k] + 1) >= mass[k+2] >= (mass[k] - 1))&((mass[k+1] + 1) >= mass[k+3] >= (mass[k+1] - 1)):
        ans = "YES"
    else:
        ans = "NO"
print(ans)
input()
    
