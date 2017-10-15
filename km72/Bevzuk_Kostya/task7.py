x = int(input("Input number1 from 1 till 8:"))
y = int(input("Input number2 from 1 till 8:"))
z = int(input("Input number3 from 1 till 8:"))
c = int(input("Input number4 from 1 till 8:"))
d = x//2
f = z//2
b = y//2
a = c//2
if x == d*2 and z == f*2  and y == b*2 and c == a*2 :
    print ("YES")
elif x == d*2+1 and z == f*2+1 and y == b*2+1 and c == a*2+1 :
    print ("YES")
elif x == z and y == c:
    print ("YES")
elif x == d*2 and z == f*2 and y == b*2+1 and c == a*2+1 :
    print("YES")
elif x == d*2+1 and z == f*2+1 and y == b*2 and c == a*2 :
    print("YES")
elif y == z and x == c:
    print ("YES")
elif y ==z and x == d*2+1 and c == d*2+1:
    print ("YES")
else:
    print("NO")
