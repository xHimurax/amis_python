queen1=[int(i) for i in input().split(" ")]
queen2=[int(i) for i in input().split(" ")]
queen3=[int(i) for i in input().split(" ")]
queen4=[int(i) for i in input().split(" ")]
queen5=[int(i) for i in input().split(" ")]
queen6=[int(i) for i in input().split(" ")]
queen7=[int(i) for i in input().split(" ")]
queen8=[int(i) for i in input().split(" ")]
z=list(zip(queen1,queen2,queen3,queen4,queen5,queen6,queen7,queen8))
for i in range(0,len(z),2):
    if z[i-1]==z[i]:
        print("NO")
for i in range(1,len(z),2):
    if z[i-1]==z[i]:
        print("NO")
for k in range(0,len(z)-1):
    if (z[k][0] + z[k][1] == z[k+1][0] + z[k+1][0])  and  (z[k][0] == z[k+1][0]) and (z[k][1] == z[k+1][1]):
        print("NO")
    else:
        print(("YES")