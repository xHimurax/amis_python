inmat = [0] *44
k=0
list = [int(e) for e in input().split()]
for e in list:
    inmat[e]+=1
for i in range(len(inmat)):
    if inmat[i]>1:
        for e in range(1,inmat[i]):
            k+=e
print(k)
