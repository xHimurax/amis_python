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
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
