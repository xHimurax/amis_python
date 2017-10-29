print('Task 4.4')
while True:
 year=int(input('Please enter the year: '))
 if year%100==0:
	 if year%400==0:
		 print('LEAP')
	 else:
		 print('COMMON')
 elif year%4==0:
 	print('LEAP')
 else:
 	print('COMMON')

