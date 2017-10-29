print('Task 4.11')
while True:
 n1=int(input('Enter the row of the first coordinate: '))
 n2=int(input('Enter the column of the first coordinate: '))
 m1=int(input('Enter the row of the second coordinate: '))
 m2=int(input('Enter the column of the second coordinate: '))
 if (abs(n1-m1)==2 or abs(n2-m2)==2) and (abs(n1-m1)==1 or abs(n2-m2)==1):
 	print('YES')
 else:
 	print('NO')
