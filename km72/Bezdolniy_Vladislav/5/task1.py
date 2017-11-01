list = input("Введите список:").split()
height = int(input("Введите высоту Пети:"))
height_ind = 0
for i in range(0, len(list)):
    a = int(list[i])
    if a >= height:
        height_ind = i + 1
print(height_ind + 1)
