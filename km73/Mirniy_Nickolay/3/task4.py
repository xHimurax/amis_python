N = int(input('Количество студентов : '))
K = int(input('Количество яблок : '))

apples = K//N
rest = K%N

if (N > 0) & (K>0) :
	print('Количество яблок у студента : ' , apples, '\nОстаток яблок : ' , rest)
else :
	print('Error')
