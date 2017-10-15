print('Task 4.7')
while True:
 n1=int(input('Enter the row of the first coordinate: '))
 n2=int(input('Enter the column of the first coordinate: '))
 m1=int(input('Enter the row of the second coordinate: '))
 m2=int(input('Enter the column of the second coordinate: '))
 if (n1-m1)%2==1 or (n2-m2)%2==1:
 	print('NO')
 else:
 	print('YES')
