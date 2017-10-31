i = 0
x =[]
y = []
a = 'NO'
while i < 8:
    x_y = input('enter x,y ').split()
    x.append(int(x_y[0]))
    y.append(int(x_y[1]))
    i += 1
for coord1 in range(0, 8):
    for coord2 in range(0, 8):
        if coord1 == coord2:
            continue
        if abs(x[coord1] - x[coord2]) == abs(y[coord1] - y[coord2]) or (x[coord2] == x[coord1] or y[coord2] == y[coord1]):
            a = 'YES'
            break
print(a)
