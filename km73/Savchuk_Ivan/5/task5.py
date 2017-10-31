a = []
i = 0
while i != 8:
    a = a + [int(i) for i in input().split()]
    i += 1
i = 0
b = []
for i in range(0, len(a), 2):
    b.append(a[i])
c = []
for i in range(1, len(a), 2):
    c.append(a[i])
d = 0
for i in range(len(b)):
    for j in range(len(c)):
        if (b[i] == b[j] and i != j) or (c[i] == c[j] and i != j) or b[0] == c[7] or (b[i] == c[i] and b[i] != 5):
            d = 1

if d == 1:
    print("YES")
else:
    print("NO")
