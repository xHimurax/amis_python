list = input("Введіть список: \n").split()
for i in list:
    i = int(i)
    if i % 2 == 0:
        print(i)    
