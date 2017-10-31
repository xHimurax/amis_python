mass = input("введите рост учеников класса через пробел - ").split()
for i in range(len(mass)):
    mass[i] = int(mass[i])
X = int(input("Введите рост Пети - "))
num = len(mass) + 1
for k in range(len(mass)):
    if X > mass[k]:
        num = num - 1
print(num)
input()
