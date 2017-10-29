a = [int(i) for i in input("Введіть список: \n").split()]
for i in range(1,len(a),2):
	t = a[i]
	a[i] = a[i-1]
	a[i-1] = t
for i in a:
	print(i, end=' ')
