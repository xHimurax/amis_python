a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
answer = ("Кількість однакових чисел:")

if a == b == c:
    print(answer,"3")
elif a == b or  b == c or a == c:
    print(answer,"2")
else:
    print(answer,"0")
