inmat = [0] *30
list = [int(e) for e in input().split()]
for e in list:
    inmat[e]+=1
for e in list:
    if inmat[e]==1:
        print(e)
