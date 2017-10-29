x = int(input("первой группе:"))
y = int(input("второй группе:"))
z = int(input("третьей группе:"))
sum = x + y + z
tableOn3Groups = sum // 2
if sum % 2 == 1:
    tableOn3Groups = 1
        
print("Мінімальну кількість столів необхідно придбати:",tableOn3Groups)
