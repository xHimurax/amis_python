x = int(input("Input number1 from 1 till 8:"))
y = int(input("Input number2 from 1 till 8:"))
z = int(input("Input number3 from 1 till 8:"))
c = int(input("Input number4 from 1 till 8:"))
if x == z or y == c:
    print("NO") 
elif abs((x+y-c+z)%2) == 0:
    print("YES")
else:
    print("NO")
