l=[]
r=[]
n, k = [int(e) for e in input().split()]
butleg = ["I"]*n
for y in range(k):
    a,b = [int(e) for e in input().split()]
    for i in range(a-1,b):
        butleg[i]="."
for e in butleg:
    print(e,end='')
    
