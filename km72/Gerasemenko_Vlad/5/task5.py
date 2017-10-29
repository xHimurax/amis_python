x =[]
y = []
answer= 'NO'
x_coord= [int(s) for s in input("Введіть список x(1-8): ").split()]
y_coord= [int(l) for l in input("Введіть список x(1-8): ").split()]
for coordx in range(0, 8):
    for coordy in range(0, 8):
        if coordx == coordy:
            continue
        if abs(x[coordx] - x[coordy]) == abs(y[coordx] - y[coordy]) or (x[coordy] == x[coordx] or y[coordy] == y[coordx]): # (abs(x2-x1) == abs(y2-y1)) or (x1 == x2 or y1 == y2)
            answer = 'YES'
            break
print(a)
# Поставьте хоть что-то за попытку *Грустное лицо*
