list = input("Введіть список: \n").split()
for i in range(len(list)):
    if list[i] != list[i-1] != list[i+1]:
        print(list[i])
