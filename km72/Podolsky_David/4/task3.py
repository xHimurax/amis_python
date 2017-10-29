print('Task 4.3')
while True:
 n1=int(input('Enter the first number: '))
 n2=int(input('Enter the second number: '))
 n3=int(input('Enter the third number: '))
 
 if n1<n2:
 	min1=n1
 else:
 	min1=n2
 	
 if n2<n3:
 	min2=n2
 else:
 	min2=n3
 	
 if min1<min2:
 	min=min1
 else:
 	min=min2
 
 if n1==n2==n3:
 	print('The numbers are equal')
 	
 print(min)
