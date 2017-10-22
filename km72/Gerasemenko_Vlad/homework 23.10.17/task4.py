list = [int(i) for i in input("Введіть список: \n").split()]
for i in range(1, len(list)):
    if list[i] > 0 and list[i - 1] > 0:
        print(list[i - 1], list[i])
    elif list[i] < 0 and list[i - 1] < 0:
        print(list[i - 1], list[i])
