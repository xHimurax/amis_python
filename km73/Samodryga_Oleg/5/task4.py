a=[]
n=int(input("Введите количество кегель "))
k=int(input("Введите количество кидков "))
for i in range (k):
    a.append((str)(i))
for i in range (k):
    li=int(input("Кегля сбитая с "))
    ri=int(input("Кегля сбитая до "))
    for li in range(ri):
        a[li]="."
    for i in range(li):
        a[i]="I"
    for ri in range(n):
        a[ri]="I"
