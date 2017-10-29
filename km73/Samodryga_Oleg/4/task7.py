a=int(input("столбец"))
b=int(input("строка"))
c=int(input("столбец"))
d=int(input("строка"))
x=int(a+b)
z=int(c+d)
if a>8 or a<1:
    a=int(input("введте столбец заново"))
elif b>8 or b<1:
    b=int(input("введте строку заново"))
elif c>8 or c<1:
    c=int(input("введте столбец заново"))
elif d>8 or d<1:
    d=int(input("введте строку заново"))
if(a==c and b==d):
    print("Вы выбрали одну и ту же клетку")
if x%2==0 and z%2==0:
    print("YES")
elif x%2==1 and z%2==1:
    print("YES")
else:
    print("NO")
input("")
