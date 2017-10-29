'''
Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:

 	
The next number for the number 179 is 180.
The previous number for the number 179 is 178.

Вхідні дані: ціле число

Вихідні дані: два рядки за наведеним у завдання форматом.
'''
n = int(input ('Ведіть число - '))
answer = 'The next number for the number', n, 'is', n+1,'\n' 'The previous number for the number', n, 'is', n-1
print(answer)
