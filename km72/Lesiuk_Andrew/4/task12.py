def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
print('Програма визначає чи можна розділити шоколадку NxM на так, щоб одна з частин матиме точно k клітин') 
while True:
    n=input('Введіть N\n')
    z=is_number(n)
    if z==True:
        n=int(n)
        break
    else:
        print('Помилка!Введіть число') 
while True:
    m=input('Введіть M\n')
    z=is_number(m)
    if z==True:
        m=int(m)
        break
    else:
        print('Помилка!Введіть число')
while True:
    k=input('Введіть K\n')
    z=is_number(k)
    if z==True:
        k=int(k)
        break
    else:
        print('Помилка!Введіть число')
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
