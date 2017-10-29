print('starting program')
x=int(input('enter year'))
if ((x%4)==0 and not((x%100)==0))or (x%400)==0:
    print('LEAP')
else:
    print('COMMON')
