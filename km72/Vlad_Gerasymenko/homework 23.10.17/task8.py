list = input("Введіть список: \n").split()
counter = len(list)
for i in list:
    i = int(i)
    if (list[i]==list[i-1]) and (i != 0):
        rez = counter-1
print(rez)
