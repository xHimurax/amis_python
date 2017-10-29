Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> q = int(input())
w = int(input())
e = int(input())
if q<=w and q<=e:
    answer=q
elif w<q and w<e :
    answer=w
else :
    answer=e
print(answer)
