a=[int(i) for i in input().split()]
z=0;
for i in a:
    for j in a:
        if i == j:
           z+=1
    z-=1       
print  (z/2)
