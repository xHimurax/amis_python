a = int(input('Количество учеников в классе №1 : '))
b = int(input('Количество учеников в классе №2 : '))
c = int(input('Количество учеников в классе №3 : '))

if (a>0)&(b>0)&(c>0) :
	answer = (a//2)+(a%2)+(b//2)+(b%2)+(c//2)+(c%2)
else :
	answer = 'Error'
	
print(answer)