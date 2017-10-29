a=int(input("Введіть число а: "))
b=int(input("Введіть число b: "))
c=int(input("Введіть число c: "))
if a==b or b==c:
    if b==c:
        print("Однакових чисел: 3")
    else:
        print("Однакових чисел: 2")
else:
    print("Однакових чисел: 0")
