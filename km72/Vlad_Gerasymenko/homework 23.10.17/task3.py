list = input("Введіть список: \n").split()
for i in range(len(list)):
    if list[i]>list[i-1] and i!=0:
        print(list[i])
