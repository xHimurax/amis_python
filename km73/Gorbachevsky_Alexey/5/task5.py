a = [[int(i) for i in input().split()] for j in range(8)]

all_pairs = [(i,j)
             for i in a
             for j in a
             if (i!=j)]

res_list = [1
            for i, j in all_pairs
            if (i[0] == j[0]) | (i[1] == j[1]) |
               (abs(i[0]-j[0]) == abs(i[1]-j[1]))]

if (len(res_list)):
    result = "YES"
else:
    result = "NO"

print(result)
