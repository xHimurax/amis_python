n, k = [int(i) for i in input().split()]
a = [[int(i)-1 for i in input().split()] for j in range(k)]
res_arr = ['I']*n
for j in a:
    for i in range(j[0], j[1]+1):
        res_arr[i] = '.'
result = "".join(res)

print(result)
