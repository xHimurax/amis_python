error=True
while error:
    n = int(input("Enter value of row: "))
    m = int(input("Enter value of column: "))
    k = int(input("Enter rest of cells: "))
    if (n>0) & (m>0) & (k>0):
        d=n*m
        if k<=d:
            if ((d%k)%n == 0) | ((d%k)%m == 0):
                print("YES")
            else:
                print("NO")
        else:
            print("Enter 'k' correctly")
            continue
        error=False
    else:
        print("Enter positive number")
