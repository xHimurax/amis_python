Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mass = input("введите рост учеников класса через пробел - ").split()
for i in range(len(mass)):
    mass[i] = int(mass[i])
X = int(input("Введите рост Пети - "))
num = len(mass) + 1
for k in range(len(mass)):
    if X > mass[k]:
        num = num - 1
print(num)
input()
