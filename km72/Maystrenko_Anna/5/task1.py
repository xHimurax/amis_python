a = input("Введіть зріст учнів >> ").split()
b = int(input("Введіть зріст Петі >> "))
b_index = 0
for i in range(0, len(a)):
    n = int(a[i])
    if n >= b:
        b_index = i + 1
print(b_index + 1)