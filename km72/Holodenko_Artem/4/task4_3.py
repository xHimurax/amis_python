a=int(input("Введіть число а: "))
b=int(input("Введіть число b: "))
c=int(input("Введіть число c: "))
if a>b:
    if b>c:
        print("min(a,b,c)=",c)
    else:
        print("min(a,b,c)=",b)
else:
    if a>c:
        print("min(a,b,c)=",c)
    else:
        print("min(a,b,c)=",a)
    
