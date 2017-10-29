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
if a==c or b==d:
    print("YES")
elif a+1==c and b+1==d:
    print("YES")
elif a+2==c and b+2==d:
    print("YES")
elif a+3==c and b+3==d:
    print("YES")
elif a+4==c and b+4==d:
    print("YES")
elif a+5==c and b+5==d:
    print("YES")
elif a+6==c and b+6==d:
    print("YES")
elif a+7==c and b+7==d:
    print("YES")
elif a-1==c and b-1==d:
    print("YES")
elif a-2==c and b-2==d:
    print("YES")
elif a-3==c and b-3==d:
    print("YES")
elif a-4==c and b-4==d:
    print("YES")
elif a-5==c and b-5==d:
    print("YES")
elif a-6==c and b-6==d:
    print("YES")
elif a-7==c and b-7==d:
    print("YES")
else:
    print("NO")
input("")
