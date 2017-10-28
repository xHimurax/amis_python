a = float(input('Длина первого катета : '))
b = float(input('Длина второго катета : '))
S = (a * b)/2

if (a>0) & (b>0) :
	answer = S

else :
	answer = 'Некорректное значение'

print(answer)