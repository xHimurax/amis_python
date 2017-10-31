x = int(input("Input number1 from 1 till 8:"))
y = int(input("Input number2 from 1 till 8:"))
z = int(input("Input number3 from 1 till 8:"))
c = int(input("Input number4 from 1 till 8:"))
if z-x == 1 and c-y == 1:
    print("YES")
elif z-x == 0 and c-y == 1:
    print("YES")
elif c-y == 0 and z-x == 1:
    print("YES")
elif x-z == 1 and y-c == 1:
    print("YES")
elif x-z == 0 and y-c == 1:
    print("YES")
elif y-c == 0 and x-z == 1:
    print("YES")
elif x == z and y == c:
    print("Yes")
else:
    print("NO")
