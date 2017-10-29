print('Task 4.12')
while True:
 n=int(input('Enter the side n: '))
 m=int(input('Enter the side m: '))
 k=int(input('Enter the amount of bricks: '))
 
 if k==n*m:
 	print('You do not need to cut chocolate bar')
 	
 x1=(n-(k/m))
 xa=x1%1
 x2=(k/m)
 xb=x2%1
 y1=(m-(k/n))
 ya=y1%1
 y2=(k/n)
 yb=y2%1
 
 if xa==0:
 	if x1>0 and x1<n:
 		print('Yes, cut side n into', x1, 'and', n-x1)
 	
 elif xb==0:
 	if x2>0 and x2<n:
 		print('Yes, cut side n into', x2, 'and', n-x2)
 		
 elif ya==0:
 	if y1>0 and y1<m:
 		print('Yes, cut side m into', y1, 'and', m-y1)
 		
 elif yb==0:
 	if y2>0 and y2<n:
 		print('Yes, cut side m into', y2, 'and', m-y2)
 		
 else:
 	print('No, you can not')
