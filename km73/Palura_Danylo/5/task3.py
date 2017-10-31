print('                 Task 3')
A=False
while not A:
####CODE
    X=[]
    list=input("Enter elements separated with 'Space'  ").split()
    for element in list:
        if list.count(str(element))==1:
            X.append(element)
####OUTPUT
    print(X)
    A = input("\nPress 'Enter' to restart\nOr enter some text to close  ")
