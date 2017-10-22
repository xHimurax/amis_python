list = input("Введіть список: \n").split()
max = int(list[0])
max_index = 0
for i in range(1, len(list)):
    n = int(list[i])
    if n > max:
        max = n
        max_index = i
print("max=",max,"max index=", max_index)
