x = []
y = []
n = 8


for i in range(n) :
	x.append(int(input('Введите x'+str(i+1) + ':' )))
	y.append(int(input('Введите y'+str(i+1)+':')))


for i in range(n) :
	for j in range(i+1 , n) :
		if (abs(x[i]-x[j])) == (abs(y[j]-y[i])) or (x[i] == x[j]) or (y[i] == y[j]):
			answer = 'Yes'
		else :
			answer = 'No'

print(answer)

