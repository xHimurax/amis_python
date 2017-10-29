a = [int(a)for a in input("Введіть список: \n").split]
counter = 0
for i in a:
    for b in a:
        if i == b:
            conter += 1
    conter -=1
print(conter // 2)
