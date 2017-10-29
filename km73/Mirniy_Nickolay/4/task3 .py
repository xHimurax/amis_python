a = int(input('First figure : '))
b = int(input('Second figure : '))
c = int(input('Third figure : '))

if (c < a) & ( c < b) :
    answer = c

elif (b < c) & (b < a) :
    answer = b

elif (a < c) & (a < b) :
    answer = a

else :
    answer = 'Error'


print(answer)