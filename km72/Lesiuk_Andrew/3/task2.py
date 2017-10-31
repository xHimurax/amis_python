print('Введіть два катети прямокутного трикутника, і отримаєте його площу. ')
while True:
    a=float(input('Введіть перший катет\n'))
    if a<=0:
        print('Катет має бути додатнім')
    else:
        break
while True:
    b=float(input('Введіть другий катет\n'))
    if b<=0:
        print('Катет має бути додатнім')
    else:
        break
print('Площа трикутника =', a*b/2)
