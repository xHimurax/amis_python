print("Enter primary coordinates of the Chess Knight")
x1 = int(input())
y1 = int(input())
print("Enter final coordinates of the Chess Knight")
x2 = int(input())
y2 = int(input())

if 0<x1<9 and 0<x2<9 and 0<y1<9 and 0<y2<9:
    if (abs(x1-x2)==2 and abs(y1-y2)==1) or (abs(x1-x2)==1 and abs(y1-y2)==2):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
