while True:
    n = int(input("Enter value of row: "))
    m = int(input("Enter value of column: "))
    k = int(input("Enter rest of cells: "))
    print()     #JUST an INDENT

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
        break
    else:
        print("Enter positive number")
        continue



