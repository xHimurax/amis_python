a = int(input("Введіть перше число >> "))
b = int(input("Введіть друге число >> "))
c = int(input("Введіть третє число >> "))

if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)