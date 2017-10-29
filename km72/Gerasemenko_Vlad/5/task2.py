list = input("Введіть список: ").split()
counter = 0
for i in list:
    i = int(i)
    if (list[i]==list[i-1]) and (i != 0):
        rez = counter + 1
print(rez)
