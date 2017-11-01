print('                 Task 4')
A=False
while not A:
### N & K control
    Int_control=False
    while not Int_control:
        N=input('Enter the number of skittles  ')
        K=input('Enter the number of throws  ')
        if N.isdigit() and K.isdigit():
            N=int(N)
            if N:
                K=int(K)
                Int_control=True
        if not Int_control:
            print('\nThe number of skittles must be integer more than 0\nThe number of throws must be integer\n')
##################
    row=['|']*N
### L & R control and playing bowling
    for i in range(1,K+1):
        LRcontrol=False
        while not LRcontrol:
            print("In "+str(i)+' trow was knocked down skittles:')
            L=input('from ')
            R=input('to ')
            if L.isdigit() and R.isdigit():
                L=int(L)
                R=int(R)
                if (1<=L) & (L<=R) & (R<=N):
                    LRcontrol=True
                    for j in range(L-1, R):
                        row[j]='.'
            if not LRcontrol:
                print('\nSpecify numbers of leftmost and rightmost downed skittles\n')
    X=''
    for i in row:
        X=X+i
####################################
    print(X)
    A = input("\nPress 'Enter' to restart\nOr enter some text to close  ")
