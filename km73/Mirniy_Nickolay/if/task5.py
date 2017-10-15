a = int(input('First number : '))
b = int(input('Second number : '))
c = int(input('Third number : '))

if (a == b)&(a == c) :
    answer = 3

elif (a == b) or (a == c ) or ( b == c ) :
    answer = 2

else :
    answer = 0

print(answer)