a = []
n = int(input('Количество элементов : '))

for i in range(n) : 
	a.append(int(input('Элемент массива : ')))

temp = 0 

for i in a :
	for j in a :
		if i == j :
			temp +=1

	temp -=1

print('Количество одинаковых пар элементов : ',temp//2)



