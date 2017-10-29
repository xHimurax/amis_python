a = input("Введіть зріст учнів: \n").split()
id = int(input())
id_index = 0
for i in range(0, len(a)):
    n = int(a[i])
    if n >= id:
        id_index = i + 1
print(id_index + 1)
