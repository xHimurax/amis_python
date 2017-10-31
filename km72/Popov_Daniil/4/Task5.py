print('starting program')
a=int(input('enter 1st number'))
b=int(input('enter 2nd number'))
c=int(input('enter 3rd number'))
if a==b and a==c:
    print('3')
elif (a==b and not a==c) or (a==c and not a==b) or (b==c and not b==a):
    print('2')
else:
    print('0')
