Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> inmat = [0] *44
k=0
list = [int(e) for e in input().split()]
for e in list:
    inmat[e]+=1
for i in range(len(inmat)):
    if inmat[i]>1:
        for e in range(1,inmat[i]):
            k+=e
print(k)
