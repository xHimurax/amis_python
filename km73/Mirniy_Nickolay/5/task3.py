a = []
n = int(input('Количество элементов : '))

for i in range(n) :
	a.append(int(input('Элемент массива : ')))

b = []
temp = 0

for element in a :
	temp = element
	if a.count(temp) == 1 :
		b.append(temp)

print(b)