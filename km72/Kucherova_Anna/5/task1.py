n = (input("Введіть зріст менше 200: ")).split()
x = int(input("Введіть зріст Петі: "))

num = 1
a = 0
for i in range(len(n)):
    a = int(n[i])
    if x >= a:
        num+=1
        print(num)
