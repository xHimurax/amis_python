
a = int(input("Введіть а: "))
b = int(input("Введіть b: "))
c = int(input("Введіть c: "))

if a == b or a == c or b == c:
    if a == b == c:
        print("3")
    else:
        print("2")
else:
    print("0")
