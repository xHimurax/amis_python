print('                 Task 2')
A=False
while not A:
    X=0
    list=input("Enter elements separated with 'Space'  ").split()
    for compared in range(0,len(list)-1):
        for element in list[compared+1:]:
            if list[compared]==element:
                X=X+1
    X='There are '+str(X)+' equal pairs of elements'
####OUTPUT
    print(X)
    A = input("\nPress 'Enter' to restart\nOr enter some text to close  ")
