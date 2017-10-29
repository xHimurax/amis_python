a = [int(i) for i in input().split()]
for i in range(0, len(a) - 1):

    if a.count(i) == 1:

        print(i)
