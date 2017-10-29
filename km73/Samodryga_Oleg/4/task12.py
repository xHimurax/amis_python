n=int(input("Кол-во строк"))
m=int(input("Кол-во столбцов"))
k=int(input("Кол-во клеток"))
s=int(n*m)
if s%2==0 and s/2==k:
    print("YES")
elif s%2==1:
    if s/2==k:
        print("YES")
    elif (s/2)+n==k
        print("YES")
    elif (s/2)+m==k
        print("YES")
else:
    print("NO")
input("")
