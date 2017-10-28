a = int(input("Введіть а:"))
b = int(input("Введіть b:"))
c = int(input("Введіть c:"))
if (a < b) & (a < c):
    print("a - найменше")
elif (b < a) & (b < c):
    print("b - найменше")
elif (c < a) & (c < b):
    print("c - найменше")
elif a == b == c:
    print("a=b=c")
else:
    print("Рахуйте самі!")
