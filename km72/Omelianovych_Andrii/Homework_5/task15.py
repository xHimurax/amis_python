count = input().split()
N = int(count[0])
K = int(count[1])
i = 0
l = []
r = []
line = [x for x in "I"*N]
while i < K:
    l_and_r = input().split()
    l.append(int(l_and_r[0]))
    r.append(int(l_and_r[1]))
    i += 1
for b in range(K+1):
    for i in (l[b], r[b]+1):
        line[i] = "."
print(line)