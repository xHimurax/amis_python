N = int(input('Количество кеглей : '))
K = int(input('Количество бросков : '))

a = []
b = []

for i in range(1 , N+1) :
	a.append(i)
for j in range(K) :
	l = int(input('От :'))
	r = int(input('До : '))
	for i in range(l , r+1 ) :
		b.append(i)

for i in a :
	if i in b :
		print('.' , end = '')

	if i not in b :
		print('I' , end = '')

		


		




