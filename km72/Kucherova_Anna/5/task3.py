n = [int(x) for x in input("Введіть числa: ").split()]
for i in range(len(n)):
    for j in range(len(n)):
        if i != j and n[i] == n[j]:
            break
    else:
        print(n[i])
