def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
print('Введіть три числа і отримайте їх суму')
while True:
    x=input('Введіть число:')
    z=is_number(x)
    if z==True:
        x=float(x)
        break
    else:
        print('Помилка!Введіть число')
if x > 0:
    print(1)
elif x == 0:
    print(0)
else:
    print(-1)
