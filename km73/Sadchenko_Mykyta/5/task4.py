n=int(input("N: "))
N=n*("I").split()
k=int(input("K: "))
l=0
r=0
list=[]
for i in range(1,k+1):
    l = int(input("l: "))
    r = int(input("r: "))
    for j in range(n):
        if l<=(j+1)<=r:
            N.pop(j)
            N.insert(j,".")
print(''.join(str(h) for h in N))