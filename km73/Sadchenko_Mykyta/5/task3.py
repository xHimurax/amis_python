list=input("list: ").split()
newList=[]
for i in list:
    if list.count(i)==1:
        newList.append(i)
for elem in newList:
    print(elem, end=" ")