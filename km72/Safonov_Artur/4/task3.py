
a = int(input("Введіть a: "))
b = int(input("Введіть b: "))
c = int(input("Введіть c: "))

if a>b:
    if b>c:
        print("Найменше число: " + str(c))
    else:
        print("Найменше число: " + str(b))
else:
    if a>c:
        print("Найменше число: " + str(c))
    else:
        print("Найменше число: " + str(a))
