list = input("Введите рост всех учеников класса поочерёдно:")
height = list.split()
for i in range (len(height)):
    height[i] = int(height[i])
X = int(input("Введите рост Пети:"))
pos = len(height) + 1
for m in range (len(height)):
    if X > height[m]:
        pos = pos - 1
print(pos)
input
