a=int(input("столбец"))
b=int(input("строка"))
c=int(input("столбец"))
d=int(input("строка"))
if a>8 or a<1:
    a=int(input("введте столбец заново"))
elif b>8 or b<1:
    b=int(input("введте строку заново"))
elif c>8 or c<1:
    c=int(input("введте столбец заново"))
elif d>8 or d<1:
    d=int(input("введте строку заново"))
if(a==c and b==d):
    print("Фигура и так в этой клетке")
if a+1==c or b==d:
    print("YES")
elif a+2==c or b==d:
    print("YES")
elif a-1==c or b==d:
    print("YES")
elif a-2==c or b==d:
    print("YES")
#-----------------------
elif a==c or b+1==d:
    print("YES")
elif a==c or b+2==d:
    print("YES")
elif a==c or b-1==d:
    print("YES")
elif a==c or b-2==d:
    print("YES")
#------------------------
elif a+1==c or b+2==d:
    print("YES")
elif a-1==c or b+2==d:
    print("YES")
elif a+1==c or b-2==d:
    print("YES")
elif a-1==c or b-2==d:
    print("YES")
#---------------------
elif a+2==c or b+1==d:
    print("YES")
elif a+2==c or b-1==d:
    print("YES")
elif a-2==c or b+1==d:
    print("YES")
elif a-2==c or b-1==d:
    print("YES")
else:
    print("NO")
input("")




