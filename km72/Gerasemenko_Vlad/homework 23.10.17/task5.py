list = input("Введіть список: \n").split()
for i in range(len(list)):
    if (list[i]>list[i-1]+list[i+1]) and (i != 0) and (i != len(list)):
        print(list[i])
