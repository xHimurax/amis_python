n = int(input("Input number1:"))
m = int(input("Input number2:"))
k = int(input("Input number3:"))
a = n//2
b = m//2
c = n*m//k
if n == a*2 or m == b*2:
    if c > 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
    
