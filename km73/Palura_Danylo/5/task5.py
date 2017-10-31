print('                 Task 5')
A=False
borders=['1', '2', '3','4', '5', '6', '7', '8']
print('The coordinates are: x - horizontal and y - vertical\ni - is number of queen\nEnter your coordinates')
while not A:
    X='\nNo'
    Q=True
    condition=True
    hor=[]
    ver=[]
    d_main=[]
    d_second=[]
    for i in range(1,9):
        control=False
        while not control:
            m=input('x('+str(i)+')')
            n=input('y('+str(i)+')')
            if borders.count(m) and borders.count(n):
                control=True
                hor.append(m)
                ver.append(n)
            if not control:
                print('Coordinates must be integers between 1 and 8\nTry again')
    for j in range(0, 8):
        if (hor.count(hor[j])!=1) or (ver.count(ver[j])!=1):
            Q=False
            break
    if Q:
        for j in range(0, 8):
            d_main.append(int(hor[j])-int(ver[j]))
            d_second.append(int(ver[7-j])-int(hor[j]))
    if Q:
        for j in range(0, 8):
            if (d_main.count(d_main[j])!=1) or (d_second.count(d_second[j])!=1):
                Q=False
                break
    if Q:
        X='\nYes'
    print(X)
    A = input("\nPress 'Enter' to restart\nOr enter some text to close  ")
