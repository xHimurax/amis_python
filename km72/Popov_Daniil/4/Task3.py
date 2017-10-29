print('starting program')
a=int(input('enter 1st number'))
b=int(input('enter 2nd number'))
c=int(input('enter 3rd number'))
if a<b and a<c:
    print(a)
elif b<c and b<a:
    print(b)
elif c<a and c<b:
    print(c)
else:
    print('some numbers are equal')
