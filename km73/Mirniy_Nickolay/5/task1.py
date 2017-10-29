height = []
people = int(input('Количество учеников в шеренге :'))

for i in range(people) :
	height.append(int(input('Рост ученика : ')))
X = int(input('Рост Пети : '))
height.append(X)


if  140 > height[i] >200 :
	answer = 'Error'

height.sort()
a = height[::-1]
b = a.count(X)
answer = a.index(X)+b
	

print('Номер Пети :' ,answer)

