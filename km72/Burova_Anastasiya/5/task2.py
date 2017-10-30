while True:
    x = input("Enter list:").split()
    count = 0
    for i in x:
        for y in x:
            if i == y:
                count = count + 1
                count = count - 1
                print(int(count/2))
