print('                 Task 1')
A=False
Q= '0123456789'
while not A:
    X=1
    control=False
    while not control:
        control=True
        CLASS=input("Enter Peter's classmates' heights separated with 'Space'  ").split()
        PETER=input("Enter Peter's height  ")
########PETER CONTROL
        for N in PETER:
            if Q.find(N)==-1:
                control=False
                break
########CLASS CONTROL
        if control:
            for child in CLASS:
                for N in child:
                    if Q.find(N)==-1:
                        control=False
                        break
                if not control:
                    break
########CONTROL OF NONEMPTINESS
        if control:
            control=bool(CLASS)
        if control:
            control=bool(PETER)
########INTATION AND 1-200 CONTROL
        if control:
            for i in range(0, len(CLASS)):
                CLASS[i]=int(CLASS[i])
                if (CLASS[i]>200) | (CLASS[i]<1):
                    control=False
                    break
            PETER=int(PETER)
            if control:
                if (PETER>200) | (PETER<1):
                    control=False
        if not control:
            print("\nUncorrect data: any height must be integer between 1 and 200\n")

########SOLVING
    for guy in CLASS:
        if guy>=PETER:
            X=X+1
    X="Peter's place is "+str(X)+'\n'
    print(X)
    A = input("\nPress 'Enter' to restart\nOr enter some text to close  ")
