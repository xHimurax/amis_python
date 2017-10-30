def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
while True:
    a=input('Введіть перше число:')
    z=is_number(a)
    if z==True:
        a=int(a)
        break
    else:
        print('Помилка!Введіть число') 
while True:
    b=input('Введіть друге число:')
    z=is_number(b)
    if z==True:
        b=int(b)
        break
    else:
        print('Помилка!Введіть число')
while True:
    c=input('Введіть третє число:')
    z=is_number(c)
    if z==True:
        c=int(c)
        break
    else:
        print('Помилка!Введіть число')
if a>b:
    if b>c:
        print(c)
    else:
        print(b)
elif b>c:
    if c<a:
        print(c)
    else:
        print(a)
else:
    if a<c:
        print(a)
    else:
        print(c)
