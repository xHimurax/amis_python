coord = [ [float(input("Enter x"+str(i))), float(input("Enter y"+str(i)))] for i in range(0,8) ]
a = "NO"
for cord1 in range(0, 8):
    for cord2 in range(0, 8):
        if cord1 == cord2:
            continue
        if (abs(coord[cord2][0]-coord[cord1][0]) == abs(coord[cord2][1]-coord[cord1][1])) or (coord[cord1][0] == coord[cord2][0] or coord[cord1][1] == coord[cord2][1]):
            a = 'YES'
            break
print(a)
# (abs(x2-x1) == abs(y2-y1)) or (x1 == x2 or y1 == y2)