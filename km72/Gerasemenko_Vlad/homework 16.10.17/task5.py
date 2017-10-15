a = int(input("Введіть а:"))
b = int(input("Введіть b:"))
c = int(input("Введіть c:"))
if a == b == c:
    print("3")
if (a == b) | (a == c) | (b == c):
    print("2")
if a!=b!=c:
    print("0")
