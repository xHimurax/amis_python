while True:
    x = input("Enter list:").split()
    count = -1
    for i in x:
        for y in  x:
            if i == y:
                count = count + 1
                if count == 0:
                    print (i, end=" ")
                    count = -1