i = 0
x =[]
y = []
a = 'NO'
while i < 8:
    x_and_y = input().split()
    x.append(int(x_and_y[0]))
    y.append(int(x_and_y[1]))
    i += 1
for cord1 in range(0, 8):
    for cord2 in range(0, 8):
        if cord1 == cord2:
            continue
        if abs(x[cord1] - x[cord2]) == abs(y[cord1] - y[cord2]) or (x[cord2] == x[cord1] or y[cord2] == y[cord1]):
            a = 'YES'
            break
print(a)
# (abs(x2-x1) == abs(y2-y1)) or (x1 == x2 or y1 == y2)