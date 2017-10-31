def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
while True:
    a=input('Введіть рік:')
    z=is_number(a)
    if z==True:
        a=int(a)
        break
    else:
        print('Помилка!Введіть число')
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('LEAP')
else:
    print('COMMON')
