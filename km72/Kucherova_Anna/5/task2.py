list = input("Введіть числа: ").split()
num = 0
for i in range(len(list)):
    i = int(i)
    if (list[i] == list[i-1]) & (i != 0):
        num+=1
        print(num)
    elif (i == 0):
        print(0)
